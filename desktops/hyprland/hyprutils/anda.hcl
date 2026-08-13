project "" {
  rpm {
    spec = "hyprutils.nightly.spec"
  }
  labels {
    nightly = 1
    subrepo = "extras"
  }
}
