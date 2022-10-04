"""Example of how to generate a time-slice image."""
import tslice2

foo = tslice2.TimeSlice("../figs/infiles/", ".jpg", verbose=True)

foo.slice(
    1,
    "../figs/outfiles/Set1_2_UD.jpg",
    borderWidth=0,
    borderCol=(255, 255, 255),
    sliceDir=1,
    verbose=True,
)

del foo
