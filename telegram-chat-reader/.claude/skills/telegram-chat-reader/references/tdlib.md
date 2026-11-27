# Установка библиотеки TDLib

Команды ниже выполняются тем Python, который запускает скилл. Под `python` подразумевается интерпретатор его виртуального окружения. Сначала проверь, может ли он уже загрузить TDLib. В каталоге установленного скилла выполни:

```sh
python -c "import sys; sys.path.insert(0, 'scripts'); from reader import TDLib; print(TDLib().version)"
```

Проверка обращается к нативной библиотеке за номером версии. Она работает до входа в Telegram. Версия 1.8.0 использует старую схему и будет отклонена.

## Быстрая установка на три платформы

Для macOS на Apple Silicon, Windows с Python x64 и Linux с glibc на x86-64 или ARM64 есть готовая сборка. Установи её в окружение скилла и повтори проверку. Пакет `tdjson` выпускает сторонний проект Python-привязок. Он включает TDLib и публикует сведения о происхождении файлов. [Пакет и список платформ](https://pypi.org/project/tdjson/1.8.71/)

```sh
python -m pip install --only-binary=:all: tdjson==1.8.71
```

Сообщение pip `No matching distribution found` означает, что для данного сочетания интерпретатора, ОС и архитектуры готовая сборка недоступна. Проверь архитектуру именно запускаемого Python через `python -c "import sysconfig; print(sysconfig.get_platform())"` и используй подходящий вариант ниже.

## macOS с системной библиотекой

Установи Homebrew по [официальной инструкции](https://brew.sh/), если его ещё нет. Для Intel Mac или установки из исходников используй формулу TDLib. Для сборки могут потребоваться Command Line Tools, их установщик открывается командой `xcode-select --install`. [Формула TDLib](https://formulae.brew.sh/formula/tdlib)

```sh
brew install --HEAD tdlib
```

Скилл автоматически ищет Homebrew-библиотеку в `/opt/homebrew` и `/usr/local`. Чтобы выбрать её явно в текущем терминале, выполни `export TDJSON_LIBRARY="$(brew --prefix tdlib)/lib/libtdjson.dylib"`.

## Linux с системной библиотекой

В Debian и Ubuntu следующий пример собирает официальную TDLib под архитектуру текущей системы. Выполняй его из рабочего каталога для сборки. Подкаталог `td` создаётся при первом клонировании. Для других дистрибутивов выбери Linux, свой дистрибутив и Python в [генераторе команд TDLib](https://tdlib.github.io/td/build.html).

```sh
sudo apt-get update
sudo apt-get install build-essential git cmake gperf php-cli libssl-dev zlib1g-dev
git clone --depth 1 https://github.com/tdlib/td.git td
cmake -S td -B td/build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_PREFIX="$HOME/.local"
cmake --build td/build --target install --parallel 2
```

После установки скилл находит `~/.local/lib/libtdjson.so` сам. Для нестандартного расположения укажи абсолютный путь в `TDJSON_LIBRARY`. Если сборке не хватает памяти, используй один параллельный процесс и рекомендации проекта по уменьшению потребления памяти. [Исходники и требования TDLib](https://github.com/tdlib/td#building)

## Windows с нативной DLL

Для нативной сборки, в том числе на Windows ARM64, установи Git, Visual Studio Build Tools с рабочей нагрузкой **Desktop development with C++** и Windows SDK. Для ARM64 включи соответствующие инструменты MSVC. Используй актуальный vcpkg и его динамический порт TDLib. [Установка vcpkg](https://learn.microsoft.com/en-us/vcpkg/get_started/get-started?pivots=shell-powershell), [пакет TDLib](https://vcpkg.io/en/package/tdlib.html)

Открой PowerShell в рабочем каталоге. Определи архитектуру запускаемого Python. Для `win-amd64` выбери `x64-windows`, для `win-arm64` — `arm64-windows`, для `win32` — `x86-windows`. Пример ниже рассчитан на x64. При существующем клоне переходи сразу в его каталог.

```powershell
python -c "import sysconfig; print(sysconfig.get_platform())"
git clone https://github.com/microsoft/vcpkg.git
Set-Location vcpkg
.\bootstrap-vcpkg.bat
$triplet = 'x64-windows'
.\vcpkg.exe install "tdlib:$triplet"
$env:TDJSON_LIBRARY = (Resolve-Path ".\installed\$triplet\bin\tdjson.dll").Path
```

Сохрани DLL в исходном каталоге `bin` вместе с зависимостями OpenSSL и zlib. Python открывает DLL по полному пути. Для следующих запусков можно сохранить значение в пользовательском окружении и перезапустить агент:

```powershell
[Environment]::SetEnvironmentVariable('TDJSON_LIBRARY', $env:TDJSON_LIBRARY, 'User')
```

Из каталога скилла повтори проверку версии в текущем PowerShell, затем в процессе агента. При ошибке загрузки проверь разрядность Python и библиотеки, наличие зависимостей рядом с DLL и рантайма MSVC. При ручной установке на любой платформе `TDJSON_LIBRARY` имеет приоритет перед готовой сборкой из Python.
