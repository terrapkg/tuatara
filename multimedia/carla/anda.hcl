project "" {
    rpm {
        spec = "Carla-nightly.spec"
    }
    labels {
        nightly = 1
        subrepo = "extras"
    }
}
