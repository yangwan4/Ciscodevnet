ip_info = {
      "TABLE_intf": {
        "ROW_intf": [
          {
            "vrf-name-out": "default",
            "intf-name": "Lo1",
            "proto-state": "up",
            "link-state": "up",
            "admin-state": "up",
            "iod": 5,
            "prefix": "1.1.1.1",
            "ip-disabled": "FALSE"
          },
          {
            "vrf-name-out": "default",
            "intf-name": "Lo2",
            "proto-state": "up",
            "link-state": "up",
            "admin-state": "up",
            "iod": 6,
            "prefix": "2.2.2.2",
            "ip-disabled": "FALSE"
          },
          {
            "vrf-name-out": "default",
            "intf-name": "Lo3",
            "proto-state": "up",
            "link-state": "up",
            "admin-state": "up",
            "iod": 7,
            "prefix": "3.3.3.3",
            "ip-disabled": "FALSE"
          },
          {
            "vrf-name-out": "default",
            "intf-name": "Eth1/2",
            "proto-state": "down",
            "link-state": "down",
            "admin-state": "down",
            "iod": 9,
            "prefix": "12.1.1.1",
            "ip-disabled": "FALSE"
          }
        ]
      }
,
  "id": 1
}

print(ip_info["TABLE_intf"]["ROW_intf"][1]["prefix"])