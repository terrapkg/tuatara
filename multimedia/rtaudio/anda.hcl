project "" {
    rpm {
        spec = "rtaudio-nightly.spec"
    }
    labels {
        nightly = 1
        subrepo = "extras"
    }
}
