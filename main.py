import sys
from ffmpeg.image_file import ImageFile
from ffmpeg.options import  ImageFileOptions
from ffmpeg.manipulater import FFmpegManipulater


in_file = sys.argv[1]
out_file = sys.argv[2]

out_file_options = ImageFileOptions()
out_file_options.set_scale(width=640)

in_file_image = ImageFile(file_name=in_file)
out_file_image = ImageFile(file_name=out_file, options=out_file_options)

manipulater = FFmpegManipulater(input_file = in_file_image, output_file=out_file_image)
manipulater.manipulate()

