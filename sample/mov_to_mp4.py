import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'/Users/01013548/video/task_property.mov':None},
    outputs={'output.mp4': None}
)
ff.run()