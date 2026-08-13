project "" {
    rpm {
        spec = "libcublas.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
