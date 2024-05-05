# Проект для экзамена по "Основам программирования" в СПбГУ

## Подбор праймеров для мультиплексной ПЦР

### Задачи:
1. Реализовать ввод фаста-файлов (гены и праймеры) и экспорт из них последовательностей в коллекции - Маша 
2. Выбирать праймеры определенной длины (15-40 нуклеотидов) - Маша
3. Реализовать совпадение праймера с последовательностью (вывести процент совпадения?) - Настя
4. Отфильтровать пары праймеров, образующих димеры - Артем
5. По результатам 3 и 4 пункта подобрать наилучшее сочетание праймер/ген - 
6. Учесть температуру отжига (опционально) - 
7. Реализовать вывод - 
8. Написать README - Артем / Настя


### Installation

Clone this repo and go to created folder: 

```shell
git clone git@github.com:ArtemVaska/multiplex_pcr_university.git && \
cd multiplex_pcr_university
```

Create mamba environment from `environment.yaml` and activate it:

```shell
mamba env create -f environment.yaml && \
mamba activate pcr
```


### Usage

```shell
python3 main.py
```
