project "" {
    rpm {
        spec = "cuda-cuobjdump.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
