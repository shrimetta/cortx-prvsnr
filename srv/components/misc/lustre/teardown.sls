{% import_yaml 'components/defaults.yaml' as defaults %}
include:
  - components.misc.lustre.start

Remove Lustre:
  pkg.purged:
    - pkgs:
      - kmod-lustre-client
      - lustre-client
      # - lustre-client-devel

Delete Lnet config file:
  file.absent:
    - name: /etc/modprobe.d/lnet.conf

Delete Lustre yum repo:
  pkgrepo.absent:
    - name: {{ defaults.lustre.repo.id }}
