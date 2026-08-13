project "" {
    rpm {
        spec = "nvidia-modprobe.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 3
    }
}
