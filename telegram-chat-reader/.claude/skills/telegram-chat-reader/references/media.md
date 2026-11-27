# Текст и звук во вложениях

Команды `history` и `media` работают без инструментов распознавания. Для TXT (UTF-8 и UTF-16 с BOM), CSV, Markdown и DOCX скиллу достаточно Python. Подключай остальные инструменты по формату первого вложения, которое хочет обработать пользователь.

## Изображения и PDF

`media --extract-text` извлекает текстовый слой PDF или распознаёт текст на изображении. Агент получает до 50 000 символов. Если PDF состоит только из отсканированных страниц, результат может быть `no_text`.

- **macOS.** Скилл вызывает системные Vision и PDFKit через Swift. Проверь `xcrun --find swift`. При отсутствии инструментов владелец устанавливает Command Line Tools через `xcode-select --install`.
- **Linux.** Для PDF нужен `pdftotext` из Poppler. Для изображений нужен Tesseract с русской и английской моделями. В Debian/Ubuntu их устанавливает `sudo apt install poppler-utils tesseract-ocr tesseract-ocr-rus tesseract-ocr-eng`. Для HEIC добавь `libheif-examples`, предоставляющий `heif-dec` или `heif-convert`. В другом дистрибутиве выбирай пакеты тех же утилит.
- **Windows.** Подойдут сборки Poppler и Tesseract для Windows. Например, в терминале **MSYS2 UCRT64** на x64 установи `pacman -S --needed mingw-w64-ucrt-x86_64-poppler mingw-w64-ucrt-x86_64-tesseract-ocr`, для HEIC также `mingw-w64-ucrt-x86_64-libheif`. Добавь каталог `ucrt64\bin` своей установки MSYS2 в PATH процесса, из которого агент запускает reader. Установи модели `rus.traineddata` и `eng.traineddata` в каталог tessdata. При отдельном каталоге укажи его в `TESSDATA_PREFIX`. [Пакет Poppler](https://packages.msys2.org/packages/mingw-w64-ucrt-x86_64-poppler), [пакет Tesseract](https://packages.msys2.org/packages/mingw-w64-ucrt-x86_64-tesseract-ocr), [модели Tesseract](https://github.com/tesseract-ocr/tessdata_fast)

На Windows и Linux выполни `pdftotext -v` и `tesseract --list-langs` из того же окружения, что и reader. Для распознавания в списке языков должны появиться `rus` и `eng`. Если скилл возвращает `missing_dependencies`, установи инструмент из поля `tools` и повтори экспорт в свободный приватный каталог. При `failed` файл также сохраняется: проверь формат, языковые модели и права доступа.

## Голосовые и видеосообщения

Для команды `transcribe` сначала используется готовая расшифровка Telegram. Если её нет, скилл преобразует звуковую дорожку в WAV через FFmpeg и распознаёт её на машине владельца через `whisper-cli`.

| Система | Установка |
| --- | --- |
| macOS | `brew install ffmpeg whisper.cpp` |
| Linux | Установи FFmpeg из пакетов дистрибутива, например `sudo apt install ffmpeg` в Debian/Ubuntu. Для whisper.cpp установи компилятор C++ и CMake, собери официальный релиз командами `cmake -B build` и `cmake --build build --config Release`. Добавь каталог с собранным `whisper-cli` в PATH. |
| Windows | Возьми сборку FFmpeg для Windows по ссылке с официального сайта и архив whisper.cpp для своей архитектуры из релизов проекта. Распакуй оба комплекта с их DLL и добавь каталоги с `ffmpeg.exe` и `whisper-cli.exe` в PATH терминала агента. Если для архитектуры нет готового архива whisper.cpp, используй его инструкцию сборки CMake с компилятором C++. |

Скачай многоязычную модель `ggml-small-q5_1.bin` в подкаталог `models` каталога сессии или передай абсолютный путь через `--model`. Проверь `ffmpeg -version` и `whisper-cli --help`. Для русского языка можно указать `--language ru`. [Сборки FFmpeg](https://ffmpeg.org/download.html), [сборка whisper.cpp](https://github.com/ggml-org/whisper.cpp), [релизы whisper.cpp](https://github.com/ggml-org/whisper.cpp/releases), [многоязычная модель](https://huggingface.co/ggerganov/whisper.cpp/blob/main/ggml-small-q5_1.bin)
