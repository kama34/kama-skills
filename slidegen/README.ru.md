# Slidegen — Генератор презентаций из AI-изображений

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Скилл для Claude Code, который генерирует полноценные презентации в виде AI-сгенерированных изображений.

## Использование

```
/slidegen <аутлайн или тема>                          Генерация с уникальным дизайном
/slidegen --preset <имя> <аутлайн>                    Генерация с пресетом стиля
/slidegen style: <описание> <аутлайн>                 Генерация с кастомным стилем
/slidegen --provider polza --model <id> <аутлайн>     Указать провайдер/модель
/slidegen --no-ref <аутлайн>                          Генерация без стилевых референсов
/slidegen --polish=N [dir]                            Итеративное улучшение качества
/slidegen --edit [dir] <комментарий>                  Редактирование существующей презентации
/slidegen --compare <dir1> <dir2>                     Сравнение двух презентаций
/slidegen --notes [dir]                               Генерация заметок спикера
/slidegen --learn=N                                   Цикл самообучения
/slidegen --create-preset <имя>                       Создать новый пресет
/slidegen --export pdf [dir]                          Собрать PDF из PNG
/slidegen --help                                      Показать справку
```

## Выходные файлы

Каждая генерация создаёт:
- `slides/slide-01.png`, `slide-02.png`, ... — отдельные слайды-изображения
- `slides.pdf` — собранный PDF
- `prompts.json` — сохранённые промпты для редактирования/перегенерации
- `meta.json` — метаданные генерации (провайдер, модель, стилевой якорь)

## Провайдер по умолчанию

Polza.ai с моделью `google/gemini-3.1-flash-image-preview`. Можно переопределить флагами `--provider` и `--model`.
