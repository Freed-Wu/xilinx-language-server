# Install

## [AUR](https://aur.archlinux.org/packages/xilinx-language-server)

```sh
yay -S python-xilinx-language-server
```

## [NUR](https://nur.nix-community.org/repos/Freed-Wu)

```nix
{ config, pkgs, ... }:
{
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import
      (
        builtins.fetchTarball
          "https://github.com/nix-community/NUR/archive/master.tar.gz"
      )
      {
        inherit pkgs;
      };
  };
  environment.systemPackages = with pkgs;
      (
        python3.withPackages (
          p: with p; [
            nur.repos.Freed-Wu.xilinx-language-server
          ]
        )
      )
}
```

## [Nix](https://nixos.org)

```sh
nix shell github:Freed-Wu/xilinx-language-server
```

Run without installation:

```sh
nix run github:Freed-Wu/xilinx-language-server -- --help
```

## [PYPI](https://pypi.org/project/xilinx-language-server)

```sh
pip install xilinx-language-server
```

See [requirements](requirements) to know `extra_requires`.
