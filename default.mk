# Normally maths formulas are rendered into MathML, which is a HTML-like format formulas
# But certain e-reader don't support MathML ; for those, GladTeX is appropriate
# GladTeX is (among other things) a Pandoc filter that renders maths formulas to SVG
GLADTEX=no 

# You can specify the filter and its option yourself
# GLADTEX_CMD=gladtex -P