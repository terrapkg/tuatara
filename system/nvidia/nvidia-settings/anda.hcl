project "" {
    rpm {
        spec = "nvidia-settings.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 3
    }
}
