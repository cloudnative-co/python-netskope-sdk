Schemas = {
    "SaaS.events": {
        "type": "object",
        "required": [
            "type", "starttime", "endtime"
        ],
        "properties": {
            "type": {
                "type": "string",
                "enum": [
                    "page",
                    "application",
                    "audit",
                    "infrastructure"
                ],
            },
            "timeperiod": {
                "type": "integer",
                "enum": [
                    3600, 86400, 604800, 2592000
                ],
                "minimum": 3600,
                "maximum": 2592000
            },
            "starttime": {
                "type": "integer",
            },
            "endtime": {
                "type": "integer",
            },
            "insertionstarttime": {
                "type": "integer",
            },
            "insertionendtime": {
                "type": "integer",
            },
            "limit": {
                "type": "integer",
                "maximum": 5000
            },
            "skip": {
                "type": "integer"
            }
        }
    },
    "SaaS.alerts": {
        "type": "object",
        "required": [
            "starttime", "endtime"
        ],
        "properties": {
            "type": {
                "type": "string",
                "enum": [
                    "anomaly", "Compromised Credential", "policy",
                    "Legal Hold", "malsite", "Malware", "DLP",
                    "Security Assessment", "watchlist", "quarantine",
                    "Remediation"
                ],
            },
            "acked": {
                "type": "boolean"
            },
            "timeperiod": {
                "type": "integer",
                "enum": [
                    3600, 86400, 604800, 2592000
                ],
                "minimum": 3600,
                "maximum": 2592000
            },
            "starttime": {
                "type": "integer"
            },
            "endtime": {
                "type": "integer"
            },
            "insertionstarttime": {
                "type": "integer"
            },
            "insertionendtime": {
                "type": "integer"
            },
            "limit": {
                "type": "integer",
                "maximum": 5000
            },
            "skip": {
                "type": "integer"
            }
        }
    },
    "SaaS.report": {
        "type": "object",
        "required": [
            "type", "starttime", "endtime"
        ],
        "properties": {
            "type": {
                "type": "string",
                "enum": [
                    "application", "connection", "alert"
                ],
            },
            "groupby": {
                "type": "string",
                "enum": [
                    "application", "user", "device", "activity"
                ],
            },
            "timeperiod": {
                "type": "integer",
                "enum": [
                    3600, 86400, 604800, 2592000
                ],
                "minimum": 3600,
                "maximum": 2592000
            },
            "starttime": {
                "type": "integer"
            },
            "endtime": {
                "type": "integer"
            },
            "limit": {
                "type": "integer",
                "maximum": 5000
            },
            "skip": {
                "type": "integer"
            }
        }
    },
    "SaaS.steeringconfig": {
        "type": "object",
        "properties": {
            "config": {
                "type": "string",
            },
            "config_id": {
                "type": "integer"
            },
            "limit": {
                "type": "integer",
                "maximum": 5000
            },
            "skip": {
                "type": "integer"
            }
        }
    },
    "SaaS.userconfig": {
        "type": "object",
        "required": [
            "email", "configtype"
        ],
        "properties": {
            "email": {
                "type": "string",
            },
            "configtype": {
                "type": "string",
                "enum": ["ios", "agent"]
            }
        }
    },
    "SaaS.quarantine": {
        "type": "object",
        "properties": {
            "op": {
                "type": "string",
                "enum": ["get-files", "download-url", "take-action"]
            },
            "quarantine_profile_id": {
                "type": "integer"
            },
            "file_id": {
                "type": "integer"
            },
        },
        "required": ["op"],
        "if": {
            "properties": {
                "op": { "const": "get-files" }
            }
        },
        "then": {
            "properties": {
                "starttime": {
                    "type": "integer"
                },
                "endtime": {
                    "type": "integer"
                }
            }
        },
        "if": {
            "properties": {
                "op": { "const": "download-url" }
            }
        },
        "then": {
            "required": ["quarantine_profile_id", "file_id"]
        },
        "if": {
            "properties": {
                "op": { "const": "take-action" }
            }
        },
        "then": {
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["block", "allow"]
                }
            },
            "required": ["quarantine_profile_id", "file_id", "action"]
        }
    },
    "SaaS.legalhold": {
        "type": "object",
        "properties": {
            "op": {
                "type": "string",
                "enum": ["get-files", "download-url", "take-action"]
            },
            "legal_hold_profile_id": {
                "type": "integer"
            },
            "file_id": {
                "type": "integer"
            },
            "type": {
                "type": "string",
                "enum": ["processed", "unprocessed"]
            }
        },
        "required": ["op"],
        "if": {
            "properties": {
                "op": { "const": "get-files" }
            }
        },
        "then": {
            "properties": {
                "starttime": {
                    "type": "integer"
                },
                "endtime": {
                    "type": "integer"
                },
            },
            "required": ["type"]
        },
        "if": {
            "properties": {
                "op": { "const": "download-url" }
            }
        },
        "then": {
            "required": ["legal_hold_profile_id", "file_id"]
        },
        "if": {
            "properties": {
                "op": { "const": "take-action" }
            }
        },
        "then": {
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["mark-processed"]
                }
            },
            "required": ["legal_hold_profile_id", "file_id", "action"]
        }
    }
}
