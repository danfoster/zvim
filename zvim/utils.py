import subprocess


def get_distro():
    output = subprocess.run(
        '. /etc/os-release && echo "$ID-$VERSION_ID"',
        stdout=subprocess.PIPE,
        shell=True,
        check=True,
    )
    return output.stdout.decode().rstrip()
