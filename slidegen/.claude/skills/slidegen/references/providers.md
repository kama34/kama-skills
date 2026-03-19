# Provider Configuration

How to call each provider's image generation API.

## Provider Resolution

1. `--provider=polza` (default if no flags) → Polza.ai
2. `--provider=openai` → OpenAI
3. `--provider=custom --base-url=<url>` → Custom endpoint

## API Key Resolution

Look up the environment variable for the resolved provider:
- Polza → `POLZA_API_KEY`
- OpenAI → `OPENAI_API_KEY`
- Custom → `CUSTOM_API_KEY`

Override with `--api-key-env=MY_VAR` to use a different variable name.

If the variable is not set, print error with setup instructions and stop. For Polza, include the registration link: https://polza.ai?referral=dA0vnQPKuQ

---

## Polza.ai

**Endpoint:** `POST https://polza.ai/api/v1/media`

**Headers:**
```
Authorization: Bearer $POLZA_API_KEY
Content-Type: application/json
```

**Default model:** `google/gemini-3.1-flash-image-preview`

**Request body (without reference):**
```json
{
  "model": "<model-id>",
  "input": {
    "prompt": "<slide prompt>",
    "aspect_ratio": "16:9",
    "image_resolution": "<1K|2K|4K>",
    "output_format": "<png|jpeg>"
  }
}
```

**Request body (with style anchor reference):**
```json
{
  "model": "<model-id>",
  "input": {
    "prompt": "<slide prompt>",
    "aspect_ratio": "16:9",
    "image_resolution": "<1K|2K|4K>",
    "output_format": "<png|jpeg>",
    "images": [
      {
        "type": "base64",
        "data": "<base64-encoded PNG of style anchor>"
      }
    ]
  }
}
```

**Image resolution and format defaults:**
- `image_resolution`: `1K` (1376x768 for 16:9), `2K` (2752x1536), `4K` (5504x3072). Set via `--resolution` flag.
- `output_format`: `jpeg` (default), `png`. Set via `--format` flag.
- These parameters go inside `input`, NOT at the top level.

**Supported aspect ratios:** 1:1, 9:16, 16:9, 3:4, 4:3, 3:2, 2:3, 5:4, 4:5, 21:9

**Response (synchronous):**
```json
{
  "id": "gen_abc123",
  "object": "media.generation",
  "status": "completed",
  "created": 1773494259,
  "model": "google/gemini-3.1-flash-image-preview",
  "data": [
    { "url": "https://s3.polza.ai/..." }
  ],
  "usage": {
    "output_units": 1,
    "cost_rub": 4.8,
    "cost": 4.8
  }
}
```

**CRITICAL:** `data` is a top-level array of objects (NOT `data.images`). Access the image URL as `data[0].url`.

**Response (async — status: "pending"):**
```json
{
  "id": "gen_abc123",
  "status": "pending"
}
```

**Async polling:**
- Poll: `GET https://polza.ai/api/v1/media/{id}` with same Authorization header
- Interval: every 5 seconds
- Per-slide timeout: 120 seconds
- On `status: "completed"`: download image from `data[0].url`
- On `status: "failed"`: log error, skip slide

**Downloading the image:**
```bash
curl -s -o <output-path> "<image-url>"
```

**Sending a generation request:**
```bash
curl -s -X POST https://polza.ai/api/v1/media \
  -H "Authorization: Bearer $POLZA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '<json-body>'
```

---

## OpenAI

**Endpoint:** `POST https://api.openai.com/v1/images/generations`

**Headers:**
```
Authorization: Bearer $OPENAI_API_KEY
Content-Type: application/json
```

**Default model:** `gpt-image-1`

**Request body:**
```json
{
  "model": "<model-id>",
  "prompt": "<slide prompt>",
  "n": 1,
  "size": "<WxH>",
  "quality": "<low|medium|high>",
  "response_format": "url"
}
```

**OpenAI quality and size defaults:**
- `size`: `1792x1024` (default). Supported: `1024x1024`, `1536x1024`, `1024x1536`, `1792x1024`, `1024x1792`. Set via `--size` flag.
- `quality`: `high` (default). Supported: `low`, `medium`, `high`. Set via `--quality` flag.

**Note:** OpenAI's `/v1/images/generations` does NOT support reference images natively. When using OpenAI provider with reference mode, include a description of the style anchor in the prompt text instead of passing an image. Append to the prompt: "Match the visual style of: [describe the anchor slide's colors, typography, layout, decorations based on Claude's visual analysis]."

**Response:**
```json
{
  "data": [
    {
      "url": "https://..."
    }
  ]
}
```

---

## Custom Provider

**Endpoint:** `POST <base-url>/v1/media` (or as specified by `--base-url`)

Uses the same request format as Polza.ai. The custom provider is assumed to be Polza-compatible (accepts `input.prompt`, `input.aspect_ratio`, `input.images`).

If the custom provider uses OpenAI format instead, the user should use `--provider=openai --base-url=<url>`.

**Headers:**
```
Authorization: Bearer $CUSTOM_API_KEY
Content-Type: application/json
```

---

## Error Handling

| HTTP Status | Action |
|---|---|
| 200-201 | Success — parse response |
| 401 | Auth error — print "Invalid API key. Check your $<VAR> environment variable." |
| 402 | Insufficient funds — print "Insufficient funds on your provider account." |
| 403 | Access denied — print "Access denied. Check your API key permissions." |
| 408 | Timeout — treat as async, try polling |
| 429 | Rate limit — exponential backoff: wait 5s, 10s, 20s (max 3 retries) |
| 500+ | Server error — retry once after 5s, then skip slide |

## Reading Reference Image as Base64

To pass the style anchor as a reference:
```bash
base64 -w 0 <path-to-anchor.png>    # Linux/Mac
# On Windows (Git Bash):
base64 -w 0 <path-to-anchor.png>
# Or with Python:
python3 -c "import base64; print(base64.b64encode(open('<path>', 'rb').read()).decode())"
```

Prepend with data URI prefix for the `images` array: `data:image/png;base64,<data>` — or send raw base64 (Polza accepts both).
