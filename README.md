> Predecessor of [applied-alpha-evolve](https://github.com/denis-samatov/applied-alpha-evolve). Shared code/results are one project lineage, not an independent second benchmark. Current development belongs there.

# Applied AlphaEvolve 🧬

*Проект направления Next-Gen LLMs в рамках Летней школы AIRI 2025*

[**Отчет**](report.pdf) | [**Презентация**](slides.pdf)

## О проекте

Недавние достижения в области автоматизированного поиска решений, примером которых является [фреймворк AlphaEvolve от Google](https://arxiv.org/pdf/2506.13131), подчеркивают эффективность интеграции больших языковых моделей с эволюционным поиском для решения сложных задач оптимизации. AlphaEvolve устанавливает новый стандарт в этой области, используя генерацию кандидатов на основе моделей и строгие механизмы оценки. В данном исследовании мы проводим сравнительный анализ трех опенсорсных эволюционных фреймворков — OpenAlpha_Evolve, OpenEvolve и MetaEvolve — на задаче оптимизации упаковки кругов, используя AlphaEvolve в качестве эталонного бенчмарка. Наш анализ охватывает как архитектуру фреймворков, так и влияние различных языковых моделей. Мы также внедряем передовые методы логирования и визуализации для более глубокого понимания эволюционного процесса и поведения различных моделей. Экспериментальные данные показывают, что MetaEvolve, использующий модели Qwen, достигает наивысшего качества решения среди открытых фреймворков (сумма радиусов = 2.6238), хотя и незначительно уступает эталону AlphaEvolve (2.635). Эта работа закладывает прочную основу для будущих исследований в области эволюционных алгоритмов, применяемых к задачам оптимизации, управляемым LLM.

## 📁 Исследуемые фреймворки

#### [`MetaEvolve`](meta_evolve/) (репозиторий без открытого доступа)

> Содержит описание и результаты бенчмаркинга, модифицирован код и продолжается работа над улучшением

- Реализация Multi-Island MAP-Elites алгоритма
- DAG-based система выполнения программ
- Асинхронная архитектура с Redis persistence
- Поддержка качественно-разнообразной оптимизации

#### [`OpenEvolve`](open_evolve/) ([репозиторий](https://github.com/codelion/openevolve))

> Содержит описание, результаты бенчмаркинга и код с нашими изменениями

- Реализация концепций AlphaEvolve от Google DeepMind
- Автоматическая генерация и оптимизация кода
- Web-интерфейс для мониторинга эволюционного процесса
- Поддержка множественных LLM провайдеров

#### [`OpenAlpha_Evolve`](open_alpha_evolve/) ([репозиторий](https://github.com/shyamsaktawat/OpenAlpha_Evolve))

> Содержит описание и результаты бенчмаркинга, не был выбран для дальнейший улучший из-за своих ограничений

- Анализ открытой реализации концепций AlphaEvolve
- Изучение агентной архитектуры и модульного дизайна
- Оценка производительности и масштабируемости
- Сравнительное исследование различных подходов к эволюционному программированию

## 🎯 Задачи

1. Изучить архитектуру и внутреннюю логику существующих реализаций AlphaEvolve (фреймворков).

2. Протестировать работу системы с различными LLM - от проприетарных больших до открытых маломощных, оценить её устойчивость и адаптируемость. Ответить на вопрос применимости такого подхода для опенсорс решений.

3. Продумать возможные улучшения:
   - Концептуальные: улучшение стратегии мутаций, адаптация метрик к задаче
   - Визуальные: более наглядная визуализация процесса эволюции
   - Технические: расширение логирования, отслеживание траектории решений


## 🛠️ Технологический стек фреймворков

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
- **Proprietary LLM via API** - OpenAI, Mistral, Gemini
- **Local LLMs via vLLMs** - Qwen, Llama, DeepSeek

## 🚀 Запуск (на примере OpenEvolve)

Системные зависимости
- Python 3.8+
- Docker (опционально)
- vLLM (для локального запуска моделей)

LLM API доступ
- OpenAI API ключ
- Mistral API ключ (опционально)

```bash
# Клонирование репозитория

# Настройка OpenEvolve  
cd airi_project/open_evolve
pip install -e .

# Настроить конфигурацию в 
# examples/circle_packing/config_phase_1.yaml
# examples/circle_packing/config_phase_2.yaml

# Запуск примера
python openevolve-run.py examples/circle_packing/initial_program.py examples/circle_packing/evaluator.py --config examples/circle_packing/config_phase_1.yaml --iterations 1
```
## Validation and execution boundary

Local code corrections do not reproduce historical model/framework superiority. Config loading, synthetic geometry and trusted-local runner tests are offline. Circle candidates use bounded numeric JSON IPC, sanitized provider environment, scratch working directory and POSIX process-group cleanup. These controls are not a hostile-code sandbox: a process can still access host files/network. Execute only reviewed, trusted local candidates here. Untrusted/generated external workloads require a separately validated sandbox with no host secrets/mounts, denied egress, CPU/memory limits and independent evaluator isolation. Generic evaluator thread timeouts limit awaiting, not underlying worker computation.

No new LLM calls or scientific results were produced. Historical private MetaEvolve throughput/production-ready descriptions are unverified author claims, not measurements independently reproduced from this public source. A valid comparison needs complete run-level data, seeds, equal token/time/evaluation budgets, all failed runs and independent feasibility replay. MetaEvolve implementation/raw experiment records are external prerequisites. Existing nested upstream workflows are not root GitHub Actions; local regression tests do not imply hosted CI ran.
