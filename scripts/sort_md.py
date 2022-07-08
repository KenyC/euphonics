# %%
import os.path
import sys
import re

files = sys.argv[1:]

"""
Desired order:

title.txt
chap1/
chap2/ ...

appendix.md

chap1/appendix/*.md

"""
# %%
regexes = [
	re.compile(r"src/title\.txt"),
	re.compile(r"src/chap(\d+)/((\d+.)*\d+).+\.md"),
	re.compile(r"src/appendix-0.md"),
	re.compile(r"src/chap(\d+)/appendix/appendix-((\d+.)*\d+).+.md"),
]

def label(f):
	for i, regex in enumerate(regexes):
		match = regex.match(f)
		if match:
			if i in [1, 3]:
				chapter_no = int(match.group(1))
				subsec = match.group(2)	
			else: 
				chapter_no = 0
				subsec = ""

			return (i, chapter_no, subsec)

# print(label("src/chap2/appendix/appendix-2.2.1-fourier-series.md"))
# print(label("src/chap3/3.4-shells-bells-saws-and-steel-pans.md"))
# files = "src/chap3/appendix/appendix-3.2.1-bending-beams-and-free-free-modes.md src/chap3/appendix/appendix-3.2.4-the-modal-density-of-a-vibrating-plate.md src/chap3/appendix/appendix-3.6.1-vibration-modes-of-a-circular-drum.md src/chap3/appendix/appendix-3.2.5-rayleighs-principle.md src/chap3/appendix/appendix-3.2.2-synthesising-percussion-sounds.md src/chap3/appendix/appendix-3.2.3-plate-vibration.md src/chap3/appendix/appendix-3.5.1-time-average-holography.md src/chap3/appendix/appendix-3.5.2-illustrating-waveguide-reflection-the-beam-on-an-elastic-foundation.md src/chap3/appendix/appendix-3.3.1-rayleighs-principle-and-tuning-a-marimba-bar.md src/chap3/appendix/appendix-3.1.1-vibration-of-an-ideal-stretched-string.md src/chap3/3.4-shells-bells-saws-and-steel-pans.md src/chap3/3.1-harmonics-and-non-harmonics.md src/chap3/3.3-marimbas-and-xylophones.md src/chap3/3.5-steel-pans-and-the-musical-saw.md src/chap3/3.6-tuned-drums.md src/chap3/3.2-beam-vibration-and-free-free-modes.md src/chap3/3-when-does-a-structure-become-a-musical-instrument.md src/appendix-0.md src/chap1/1-introduction.md src/chap2/2.2-frequency-analysis-and-modes.md src/chap2/appendix/appendix-2.2.3-linearity-for-small-vibration.md src/chap2/appendix/appendix-2.2.8-impulse-response-and-convolution.md src/chap2/appendix/appendix-2.1.1-linearity-and-sine-waves.md src/chap2/appendix/appendix-2.2.5-vibration-frequency-response.md src/chap2/appendix/appendix-2.2.1-fourier-series.md src/chap2/appendix/appendix-2.2.6-frequency-spectrum-of-a-hammer-tap.md src/chap2/appendix/appendix-2.2.4-degenerate-modes-of-a-drum.md src/chap2/appendix/appendix-2.2.2-the-undamped-harmonic-oscillator.md src/chap2/appendix/appendix-2.2.7-vibration-damping.md src/chap2/2-underpinnings-i-good-vibrations.md src/chap2/2.4-images-of-vibration.md src/chap2/2.3-frequency-and-pitch.md src/chap2/2.1-linear-and-nonlinear.md src/title.txt".split(" ")
sorted_files =sorted(files, key = label)


print(" ".join(sorted_files), end = "")

# def comp(f1, f2):
# 	if f1 == "src/title.txt":
# 		return True
# 	if f2 == "src/title.txt":
# 		return False


# def get_info(f):
# 	directory, filename = os.path.split(f)



# # quickest to implement sort
# for i in range(n):
# 	for j in range(n)
# 		if comp(files[j], files[i]):
# 			files[j], files[i] = files[i], files[j]