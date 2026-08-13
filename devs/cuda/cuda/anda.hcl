project "" {
    rpm {
	spec = "cuda.spec"
	}
	labels {
	   subrepo = "nvidia"
	   updbranch = 1
    }
}
