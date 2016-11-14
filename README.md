# 12_image_resize

## Описание

Скрипт предназначен для изменения размера изображений формата: jpg, png, gif, bmp.

Логика работы скрипта:

1. Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. И наоборот.
2. Если указана и ширина и высота – создается именно такое изображение, при этом в консоль  выводится предупреждение,
если пропорции не совпадают с пропорциями исходного изображения.
3. Если указан масштаб, то ширина и высота указаны быть не могут.
4. Если не указан путь до финального файла, то результат кладётся рядом с исходным файлом.
5. Имя изображения на выходе точно такое же, как и на входе, дополненное лишь новыми размерами. Формат сохраняется.

## Как использовать

Введите в консоли:
`python image_resize.py PATH_TO_IMAGE [optional arguments]`

PATH_TO_IMAGE - обязательный параметр.

optional arguments:

1. `--width WIDTH`
2. `--height HEIGHT`
3. `--scale SCALE`
4. `--path_to_save PATH_TO_SAVE`

*Ограничения:

1. Параметры width и height должны быть целыми, положительным числами, scale - положительным действительным,
path_to_save - строкой.
2. Параметр scale не может быть задан одновременно с параметрами width и height.