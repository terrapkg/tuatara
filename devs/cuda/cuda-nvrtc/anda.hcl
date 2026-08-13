project "" {
    rpm {
        spec = "cuda-nvrtc.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
