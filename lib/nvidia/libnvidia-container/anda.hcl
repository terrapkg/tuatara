project "" {
    rpm {
        spec = "libnvidia-container.spec"
    }
    labels = {
        subrepo = "nvidia"
        mock = 1
    }
}
