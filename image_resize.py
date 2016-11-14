import os
import argparse
from PIL import Image


def check_positive_float(value):
    ivalue = float(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Scale (%s) should be positive." % value)
    return ivalue


def resize_image(path_to_original, path_to_result, width, height, scale):
    img = Image.open(path_to_original)
    img_name, img_ext = os.path.splitext(path_to_original)
    k = get_ratio(*img.size)
    if scale:
        width, height = img.size
        resized_image = img.resize([round(width * scale), round(height * scale)])
    elif width and height:
        if width / height != k:
            print_scale_warning()
        resized_image = img.resize([width, height])
    elif width:
        resized_image = img.resize([width, round(width / k)])
    elif height:
        resized_image = img.resize([round(height * k), height])
    else:
        return 0
    return save_resized_img(
                resized_image,
                img_name=img_name,
                img_ext=img_ext,
                path_to_result=path_to_result
            )


def get_ratio(original_width, original_height):
    return original_width / original_height


def save_resized_img(resized_img, img_name, img_ext, path_to_result):
    scale_fmt = '%sx%s' % resized_img.size
    img_fmt = get_img_format(img_ext)
    if path_to_result and os.path.exists(path_to_result):
        output = "%s/%s__%s%s" % (path_to_result, img_name, scale_fmt, img_ext)
        resized_img.save(output, img_fmt)
        return print_result_of_saving(output)
    else:
        output = "%s__%s%s" % (img_name, scale_fmt, img_ext)
        resized_img.save(output, img_fmt)
        return print_result_of_saving(output)


def get_img_format(img_ext):
    if 'jpg' in img_ext:
        return 'jpeg'
    elif 'png' in img_ext:
        return 'png'
    elif 'bmp' in img_ext:
        return 'bpm'


def print_result_of_saving(saved_file):
    file_name = os.path.basename(saved_file)
    print("Resized image with name '%s' was saved here: %s." % (file_name, saved_file))


def print_scale_warning():
    print("Warning! You change ratio WIDTH/HEIGHT.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument("path", help="The path to image you want to resize.", type=str)

    group = parser.add_argument_group()
    group.add_argument("--width", help="Weight to resize image.", type=int)
    group.add_argument("--height", help="Height to resize image.", type=int)
    scale_arg = group.add_argument("--scale", help="Scale to resize image.", type=check_positive_float)
    parser.add_argument("--path_to_save", help="The path where you want to save image.", type=str)

    args = parser.parse_args()
    if args.scale and (args.width or args.height):
        raise argparse.ArgumentError(scale_arg, "You can't set scale and width/height at the same time.")
    else:
        resize_image(
            path_to_original=args.path,
            path_to_result=args.path_to_save,
            width=args.width,
            height=args.height,
            scale=args.scale
        )
