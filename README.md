# AIRI Project: Эволюционное программирование и качественно-разнообразная оптимизация 🧬

## Обзор

Данный репозиторий содержит коллекцию исследований, анализов и разработок в области **эволюционного программирования** и **качественно-разнообразной оптимизации**, выполненных в рамках исследовательской деятельности на **Летней Школе AIRI**.

Проект фокусируется на изучении современных подходов к автоматическому синтезу и оптимизации программ с использованием эволюционных алгоритмов, больших языковых моделей и гибридных методов.

## 🗂️ Структура репозитория

### 📁 Основные проекты

#### [`metaevolve/`](metaevolve/)
**Высокопроизводительный фреймворк эволюционных вычислений**
- Реализация Multi-Island MAP-Elites алгоритма
- DAG-based система выполнения программ
- Асинхронная архитектура с Redis persistence
- Поддержка качественно-разнообразной оптимизации

#### [`openevolve/`](openevolve/)  
**Система эволюции кода с помощью LLM**
- Реализация концепций AlphaEvolve от Google DeepMind
- Автоматическая генерация и оптимизация кода
- Web-интерфейс для мониторинга эволюционного процесса
- Поддержка множественных LLM провайдеров

#### [`open_alpha_envolve/`](open_alpha_envolve/)
**Исследование OpenAlpha_Evolve**
- Анализ открытой реализации концепций AlphaEvolve
- Изучение агентной архитектуры и модульного дизайна
- Оценка производительности и масштабируемости
- Сравнительное исследование различных подходов к эволюционному программированию

### 📊 Аналитические отчеты

#### [`meta_envolve/`](meta_envolve/)
**Технический анализ MetaEvolve**
- Архитектурный обзор и оценка производительности
- Анализ преимуществ и ограничений
- Результаты тестирования на benchmark задачах

#### [`open_envolve/`](open_envolve/)
**Технический анализ OpenEvolve** 
- Исследование архитектуры и компонентов
- Оценка применимости и масштабируемости
- Практические рекомендации по использованию

#### [`open_alpha_envolve/`](open_alpha_envolve/)
**Технический анализ OpenAlpha_Evolve**
- Детальное изучение открытой реализации концепций AlphaEvolve
- Анализ агентной архитектуры (PromptDesignerAgent, CodeExecutorAgent, ValidatorAgent)
- Оценка модульности и расширяемости системы
- Сравнительный анализ с альтернативными подходами
- Исследование производительности и масштабируемости
- Выявление архитектурных ограничений и возможностей оптимизации
- Практические рекомендации по применению и развертыванию

## 🎯 Исследовательские направления

### Основные области исследований

1. **Quality-Diversity Optimization**
   - MAP-Elites и его вариации
   - Multi-objective эволюционные алгоритмы
   - Архивные стратегии и behavior characterization

2. **LLM-Guided Evolution**
   - Эволюция промптов и кода
   - Гибридные методы gradient-free оптимизации
   - Автоматический синтез алгоритмов

3. **Program Synthesis & Optimization**
   - Нейроархитектурный поиск (NAS)
   - Автоматическая оптимизация программ
   - Scientific discovery через code evolution

4. **Scalable Evolutionary Computing**
   - Асинхронные и distributed алгоритмы
   - Pipeline-based архитектуры
   - Performance engineering для эволюционных систем

## 🛠️ Технологический стек

### Основные технологии
- **Python 3.8+** - основной язык разработки
- **AsyncIO** - асинхронное программирование
- **Redis** - высокопроизводительное хранение состояния
- **Docker** - контейнеризация и изоляция

### Фреймворки и библиотеки
- **Pydantic** - валидация данных и типизация
- **Loguru** - структурированное логирование
- **NumPy** - численные вычисления
- **FastAPI** - веб-интерфейсы и API

### LLM интеграции
- **OpenAI API** - GPT-4, GPT-3.5
- **Mistral AI** - Mistral 7B, Mixtral
- **Anthropic Claude** - исследовательские эксперименты

## 📈 Ключевые результаты

### Производительность
- **MetaEvolve**: 100-500+ программ/сек на стандартном hardware
- **Масштабируемость**: поддержка 4-16+ параллельных островов
- **Эффективность**: <1GB памяти для 10k+ программ в популяции

### Качество оптимизации
- **Circle Packing**: достижение результата 2.0664 (26 кругов)
- **Success Rate**: 99.2% на benchmark задачах
- **Конвергенция**: стабильная в пределах 25 поколений

### Техническая зрелость
- **Production-ready** архитектура с fault tolerance
- **Comprehensive monitoring** и system observability
- **Checkpoint/restart** механизмы для длительных экспериментов

### Аналитические достижения
- **Глубокий анализ OpenAlpha_Evolve**: выявление сильных и слабых сторон агентной архитектуры
- **Архитектурные insights**: детальная оценка модульности и расширяемости систем
- **Производительностный benchmarking**: сравнительный анализ различных подходов к эволюционному программированию
- **Практические рекомендации**: конкретные guidelines по применению и оптимизации

## 🔬 Научные вклады

### Методологические инновации
1. **Hybrid LLM-Evolution Pipeline** - интеграция языковых моделей в эволюционный процесс
2. **Adaptive Behavior Spaces** - динамическая настройка пространства характеристик
3. **Multi-Island Coordination** - эффективные стратегии миграции и специализации

### Архитектурные решения
1. **DAG-Based Execution** - гибкие пайплайны для program evaluation
2. **Async-First Design** - высокопроизводительная обработка больших популяций
3. **Redis-Backed Persistence** - надежное хранение эволюционного состояния

## 🎓 Применения и кейсы

### Исследовательские приложения
- **Neural Architecture Search** для computer vision
- **Algorithmic Discovery** в computational science
- **Creative AI** для генеративного искусства
- **Automated Programming** для domain-specific tasks

### Benchmark задачи
- **Geometric Optimization** (Circle/Hexagon Packing)
- **Function Minimization** (mathematical optimization)
- **Code Generation** (programming challenges)
- **Scientific Computing** (numerical algorithms)

### Сравнительные исследования
- **Анализ OpenAlpha_Evolve**: сравнение агентной vs pipeline архитектур
- **Evaluation различных LLM-guided подходов**: OpenEvolve vs OpenAlpha_Evolve vs MetaEvolve
- **Performance benchmarking**: метрики эффективности различных реализаций
- **Архитектурные trade-offs**: анализ модульности vs производительности

## 🚀 Быстрый старт

### Предварительные требования
```bash
# Системные зависимости
- Python 3.8+
- Redis Server
- Docker (опционально)

# LLM API доступ
- OpenAI API ключ
- Mistral API ключ (опционально)
```

### Установка и запуск
```bash
# Клонирование репозитория
git clone <repository-url>
cd airi_project

# Настройка MetaEvolve
cd metaevolve
pip install -e .

# Настройка OpenEvolve  
cd ../openevolve
pip install -e .

# Запуск примера
python examples/circle_packing/run_evolution.py
```

## 📚 Документация

Каждый подпроект содержит детальную документацию:

- [`metaevolve/README.md`](metaevolve/README.md) - техническое руководство по MetaEvolve
- [`openevolve/README.md`](openevolve/README.md) - руководство пользователя OpenEvolve

### Аналитические отчеты:
- [`meta_envolve/README.md`](meta_envolve/README.md) - технический анализ архитектуры MetaEvolve
- [`open_envolve/README.md`](open_envolve/README.md) - исследование системы OpenEvolve
- [`open_alpha_envolve/README.md`](open_alpha_envolve/README.md) - комплексный анализ OpenAlpha_Evolve с оценкой агентной архитектуры

## 🤝 Участие в проекте

Данные проекты разработаны в рамках исследовательской деятельности AIRI и предназначены для академического использования. 

### Контакты и сотрудничество
Для вопросов по исследованию и возможного сотрудничества обращайтесь к исследовательской группе AIRI.

## 📄 Лицензирование

Проекты используют MIT лицензию для открытых компонентов. Некоторые исследовательские разработки могут иметь ограниченный доступ.

## 🔗 Связанные исследования

### Основополагающие работы
- **AlphaEvolve**: "A coding agent for scientific and algorithmic discovery" (Google DeepMind, 2025)
- **MAP-Elites**: "Illuminating search spaces by mapping elites" (Mouret & Clune, 2015)
- **Quality-Diversity**: "Quality and Diversity Optimization: A Unifying Modular Framework" (Cully & Demiris, 2017)

### Связанные проекты
- [OpenAlpha_Evolve](https://github.com/shyamsaktawat/OpenAlpha_Evolve) - открытая реализация AlphaEvolve
- [OpenEvolve](https://github.com/codelion/openevolve) - альтернативная реализация эволюционного программирования

---

**AIRI (Artificial Intelligence Research Institute)**  
*Advancing the frontiers of artificial intelligence through fundamental research*

---

*Последнее обновление: январь 2025* 