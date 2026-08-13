project "" {
    rpm {
        spec = "cuda-gdb.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
