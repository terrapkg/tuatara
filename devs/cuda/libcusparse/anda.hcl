project "" {
    rpm {
        spec = "libcusparse.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
