project "" {
    rpm {
        spec = "libcuobjclient.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
