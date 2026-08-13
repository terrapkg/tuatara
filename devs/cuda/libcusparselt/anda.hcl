project "" {
    rpm {
        spec = "libcusparselt.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
