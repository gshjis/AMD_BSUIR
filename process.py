import os

def concatenate_video(input_file, output_file, times):
    command = f"ffmpeg -i {input_file} --stream_loop {times} -c copy {output_file}"
    os.system(command)

if __name__ == "__main__":
    input_file = "amd/plot.mp4"
    output_file = "amd/concatenated_plot.mp4"
    times = 4
    concatenate_video(input_file, output_file, times)
