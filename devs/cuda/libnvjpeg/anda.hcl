project "" {
    rpm {
        spec = "libnvjpeg.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
