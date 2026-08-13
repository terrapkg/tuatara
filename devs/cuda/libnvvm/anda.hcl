project "" {
    rpm {
        spec = "libnvvm.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
