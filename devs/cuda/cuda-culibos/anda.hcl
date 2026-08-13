project "" {
    rpm {
        spec = "cuda-culibos.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
