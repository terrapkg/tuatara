project "" {
    rpm {
        spec = "cuda-cuxxfilt.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
