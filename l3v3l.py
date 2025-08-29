[ {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "ebea1cbf-0b72-427f-bf5d-533adbf0c3e6",
   "id": "ahfgeienlihckogmohjhadlkjgocpleb",
   "location": "COMPONENT",
   "manifest_version": 1,
   "name": "Web Store",
   "path": "/opt/google/chrome/resources/web_store",
   "permissions": {
      "active": {
         "api": [ "management", "system.display", "system.storage", "webstorePrivate", "system.cpu", "system.memory", "system.network" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_HOSTED_APP",
   "version": "0.2"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 4,
      "listeners": [ {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://bpmcpldpdmajfigpchkicefoigmkfalc/"
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://bpmcpldpdmajfigpchkicefoigmkfalc/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://bpmcpldpdmajfigpchkicefoigmkfalc/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://bpmcpldpdmajfigpchkicefoigmkfalc/"
      } ]
   },
   "guid": "c60cab16-b7ee-4db5-80f3-fdb83048b80e",
   "id": "bpmcpldpdmajfigpchkicefoigmkfalc",
   "location": "COMPONENT",
   "manifest_version": 3,
   "name": "Basic Editor for Office files",
   "path": "/usr/share/chromeos-assets/quickoffice",
   "permissions": {
      "active": {
         "api": [ "clipboardRead", "clipboardWrite", "cookies", "downloads", "fileSystem", "fileSystem.write", "identity", "identity.email", "metricsPrivate", "storage", "unlimitedStorage" ],
         "explicit_hosts": [ "*://*.google.com/*", "https://www.google-analytics.com/*", "https://www.googleapis.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "151.137.139"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 1,
      "listeners": [ {
         "event_name": "app.runtime.onLaunched",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "85dc172f-9c5d-4d1c-a43b-3a71b61bc890",
   "id": "cnbgggchhmkkdmeppjobngjoejnihlei",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Play Store",
   "path": "/opt/google/chrome/resources/chromeos/arc_support",
   "permissions": {
      "active": {
         "api": [ "browser", "nativeMessaging", "webview" ],
         "explicit_hosts": [ "chrome://resources/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_PLATFORM_APP",
   "version": "0.2.0.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 4,
      "listeners": [ {
         "event_name": "ttsEngine.onPause",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onResume",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onSpeakWithAudioStream",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onStop",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "c1d5af19-4e44-4ee1-9661-c9b36c3d19c5",
   "id": "dakbfdmgjiabojdgbiljlhgjbokobjpg",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "eSpeakNG text-to-speech extension",
   "path": "/usr/share/chromeos-assets/speech_synthesis/espeak-ng",
   "permissions": {
      "active": {
         "api": [ "storage", "ttsEngine" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.49.3.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 14,
      "listeners": [ {
         "event_name": "action.onClicked",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "action.onClicked",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "cookies.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "cookies.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://dikiaagfielfbnbbopidjjagldjopbpa/"
      } ]
   },
   "guid": "eb23197f-cdf4-40f1-97a2-74a8bdde724c",
   "id": "dikiaagfielfbnbbopidjjagldjopbpa",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Clever Plus",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/dikiaagfielfbnbbopidjjagldjopbpa/1.18.4_0",
   "permissions": {
      "active": {
         "api": [ "activeTab", "cookies", "gcm", "identity", "identity.email", "idle", "storage", "tabs", "enterprise.deviceAttributes", "scripting" ],
         "explicit_hosts": [ "*://*/*", "https://clever.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [ "*://*/*", "*://localhost/in/*", "https://*.int.clever.com/in/*", "https://clever.com/in/*" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.18.4"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 6,
      "listeners": [ {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      }, {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s1",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s1",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://donbapingkdboklmjcfmpagmdohkgphg/"
      } ]
   },
   "guid": "83c7504c-0e94-43ed-852d-5ccb600a51b2",
   "id": "donbapingkdboklmjcfmpagmdohkgphg",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Smoothwall Safeguarding Client (Global)",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/donbapingkdboklmjcfmpagmdohkgphg/4.2.7.44749_0",
   "permissions": {
      "active": {
         "api": [ "alarms", "background", "identity", "identity.email", "storage", "tabs", "unlimitedStorage", "webRequest", "enterprise.deviceAttributes", "enterprise.networkingAttributes", "scripting" ],
         "explicit_hosts": [ "\u003Call_urls>", "http://*/*", "https://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [ "\u003Call_urls>" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "4.2.7.44749"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 45,
      "listeners": [ {
         "event_name": "action.onClicked",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "action.onClicked",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "contextMenus.onClicked",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "contextMenus.onClicked",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onGetCapabilityRequested",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onGetCapabilityRequested",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onGetPrintersRequested",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onGetPrintersRequested",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onPrintRequested",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "printerProvider.onPrintRequested",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webNavigation.onBeforeNavigate",
         "filter": {
            "url": [ {
               "pathSuffix": ".pdf",
               "urlPrefix": "file://"
            }, {
               "pathSuffix": ".PDF",
               "urlPrefix": "file://"
            } ]
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webNavigation.onBeforeNavigate",
         "filter": {
            "url": [ {
               "pathSuffix": ".pdf",
               "urlPrefix": "file://"
            }, {
               "pathSuffix": ".PDF",
               "urlPrefix": "file://"
            } ]
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s2",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s2",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s3",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s3",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s5",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s5",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s8",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onCompleted/s8",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onErrorOccurred/s4",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onErrorOccurred/s4",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s6",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s6",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s7",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s7",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onSendHeaders/s1",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "webRequest.onSendHeaders/s1",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/"
      } ]
   },
   "guid": "27963281-1d98-4772-a5b1-40a6fdc13528",
   "id": "ecnphlgnajanjnkcmbpancdjoidceilk",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Kami for Google Chromeâ„¢",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/ecnphlgnajanjnkcmbpancdjoidceilk/2.0.21120_0",
   "permissions": {
      "active": {
         "api": [ "contextMenus", "printerProvider", "storage", "tabs", "webNavigation", "webRequest", "declarativeNetRequest", "scripting", "offscreen" ],
         "explicit_hosts": [ "\u003Call_urls>" ],
         "manifest": [  ],
         "scriptable_hosts": [ "\u003Call_urls>", "https://*.instructure.com/*/assignments/*", "https://*.instructure.com/*/assignments/*/edit*", "https://*.instructure.com/*/assignments/new*", "https://*.kami.systems/web/*", "https://*.kamihq.com/web/*", "https://*.kamipdf.com/web/*", "https://*.officeapps.live.com/*", "https://*.onedrive.live.com/*", "https://*.sharepoint.com/*p*/r/*", "https://*.sharepoint.com/*w*/r/*", "https://app.peardeck.com/*", "https://assignments.onenote.com/*", "https://classroom.google.com/*", "https://classroom.google.com/*g/tg/*", "https://docs.google.com/*", "https://docs.google.com/document/d/*", "https://docs.google.com/presentation/d/*", "https://docs.google.com/spreadsheets/d/*", "https://drive.google.com/*", "https://drive.google.com/picker*", "https://jamboard.google.com/*", "https://jamboard.google.com/d/*", "https://tealearn.instructure.com/courses/*/pages/*", "https://www.canva.com/design/*", "https://www.teacherspayteachers.com/**" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "2.0.21120"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 7,
      "listeners": [ {
         "event_name": "contextMenus.onClicked",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://epkahbohdeajpadlmelfkenmoeblkpem/"
      }, {
         "event_name": "contextMenus.onClicked",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://epkahbohdeajpadlmelfkenmoeblkpem/"
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://epkahbohdeajpadlmelfkenmoeblkpem/"
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://epkahbohdeajpadlmelfkenmoeblkpem/"
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "storage.local.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      } ]
   },
   "guid": "ab5e118b-9adf-460d-8faf-df4dd326d426",
   "id": "epkahbohdeajpadlmelfkenmoeblkpem",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Linewize Filter Content Aware - Image blurring",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/epkahbohdeajpadlmelfkenmoeblkpem/1.0.104_0",
   "permissions": {
      "active": {
         "api": [ "activeTab", "contextMenus", "cookies", "storage", "tabs", "webNavigation", "webRequest", "scripting" ],
         "explicit_hosts": [ "*://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [ "\u003Call_urls>" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.0.104"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 1,
      "listeners": [ {
         "event_name": "app.runtime.onLaunched",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "a19cd7a0-eda7-40c3-abe1-eada73d3fa78",
   "id": "faknnniaockbfopbocflpciojcekfped",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 2,
   "name": "BIG IDEAS MATH",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/faknnniaockbfopbocflpciojcekfped/1.1.1_0",
   "permissions": {
      "active": {
         "api": [ "fileSystem", "fileSystem.write", "identity", "storage", "unlimitedStorage" ],
         "explicit_hosts": [ "http://*/*", "https://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_PLATFORM_APP",
   "version": "1.1.1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE", "WAS_INSTALLED_BY_DEFAULT" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 2,
      "listeners": [ {
         "event_name": "alarms.onAlarm",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ghbmnnjooekpmoecnnnilnnbdlolhkhi/"
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ghbmnnjooekpmoecnnnilnnbdlolhkhi/"
      } ]
   },
   "guid": "fccf1f36-b3d3-4613-b7a7-513be15edcb8",
   "id": "ghbmnnjooekpmoecnnnilnnbdlolhkhi",
   "location": "EXTERNAL_PREF_DOWNLOAD",
   "manifest_version": 3,
   "name": "Google Docs Offline",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.95.1_0",
   "permissions": {
      "active": {
         "api": [ "alarms", "storage", "unlimitedStorage", "offscreen" ],
         "explicit_hosts": [ "https://docs.google.com/*", "https://drive.google.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.95.1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 4,
      "listeners": [ {
         "event_name": "ttsEngine.onPause",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onResume",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onSpeak",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "ttsEngine.onStop",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "c58c24a5-d1c8-4ba6-b261-6dd9cec139cc",
   "id": "gjjabgpgjpampikjhjpfhneeoapjbjaf",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Chrome OS built-in text-to-speech extension",
   "path": "/usr/share/chromeos-assets/speech_synthesis/patts",
   "permissions": {
      "active": {
         "api": [ "accessibilityPrivate", "metricsPrivate", "tts", "ttsEngine", "unlimitedStorage" ],
         "explicit_hosts": [ "https://*.gvt1.com/*", "https://dl.google.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "29.6"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE", "WAS_INSTALLED_BY_DEFAULT" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 4,
      "listeners": [ {
         "event_name": "runtime.onStartup",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://gndmhdcefbhlchkhipcnnbkcmicncehk/"
      }, {
         "event_name": "runtime.onStartup",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://gndmhdcefbhlchkhipcnnbkcmicncehk/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://gndmhdcefbhlchkhipcnnbkcmicncehk/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://gndmhdcefbhlchkhipcnnbkcmicncehk/"
      } ]
   },
   "guid": "ac00df0e-d9a1-4200-b306-5d59bdeb3be0",
   "id": "gndmhdcefbhlchkhipcnnbkcmicncehk",
   "location": "EXTERNAL_COMPONENT",
   "manifest_version": 3,
   "name": "Assessment Assistant",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/gndmhdcefbhlchkhipcnnbkcmicncehk/24.311.1_0",
   "permissions": {
      "active": {
         "api": [ "devtools", "enterprise.platformKeys", "management", "storage", "tabs", "webNavigation", "lockWindowFullscreenPrivate" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "24.311.1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 2,
      "listeners": [ {
         "event_name": "app.runtime.onLaunched",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "commands.onCommand",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "736889c8-14b8-4712-87af-210c43f1365f",
   "id": "gngadipbljmmcgcjjflidckpbgebnhod",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 2,
   "name": "Riverside DataManager",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/gngadipbljmmcgcjjflidckpbgebnhod/0.0.0.12_0",
   "permissions": {
      "active": {
         "api": [ "audioCapture", "clipboardWrite", "storage", "system.display", "tts", "videoCapture", "webview" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_PLATFORM_APP",
   "version": "0.0.0.12"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 1,
      "listeners": [ {
         "event_name": "app.runtime.onLaunched",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "93420d9c-0f30-4cc0-b142-1aef47bd62c5",
   "id": "hmbjbjdpkobdjplfobhljndfdfdipjhg",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 2,
   "name": "Zoom",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/hmbjbjdpkobdjplfobhljndfdfdipjhg/5.0.4301.407_0",
   "permissions": {
      "active": {
         "api": [ "app.window.alwaysOnTop", "audioCapture", "desktopCapture", "fileSystem", "fileSystem.directory", "fileSystem.write", "idle", "power", {
            "socket": [ "tcp-connect:*:*", "udp-bind:*:*", "udp-send-to:*:*", "resolve-host", "resolve-proxy" ]
         }, "storage", "system.display", "unlimitedStorage", "videoCapture", "webview", "system.cpu", "system.memory" ],
         "explicit_hosts": [ "*://*.zoom.com/*", "*://*.zoom.us/*", "*://*.zoomdev.us/*", "*://*.zoomgov.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_PLATFORM_APP",
   "version": "5.0.1 (4301.0407)"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "075adb11-f205-4cf6-b470-3f17f7a914d7",
   "id": "hmffdimoneaieldiddcmajhbjijmnggi",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "EasyBib Toolbar",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/hmffdimoneaieldiddcmajhbjijmnggi/1.0.0_0",
   "permissions": {
      "active": {
         "api": [ "storage", "tabs" ],
         "explicit_hosts": [ "*://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [ "*://*/*" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.0.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "8baba9e0-ff9d-4f33-ad53-40d4704c67dd",
   "id": "honijodknafkokifofgiaalefdiedpko",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Help",
   "path": "/usr/share/chromeos-assets/helpapp",
   "permissions": {
      "active": {
         "api": [ "storage" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "4.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 68,
      "listeners": [ {
         "event_name": "alarms.onAlarm",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "alarms.onAlarm",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "identity.onSignInChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "identity.onSignInChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "idle.onStateChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "idle.onStateChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "runtime.onInstalled",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "runtime.onStartup",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "runtime.onStartup",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "storage.managed.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "storage.managed.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onAttached",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onAttached",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onCreated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onCreated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onReplaced",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onReplaced",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webNavigation.onCommitted",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webNavigation.onCommitted",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onAuthRequired/s11",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onAuthRequired/s11",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s10",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s10",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s16",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s16",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s1",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s1",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s15",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s15",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s2",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s2",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s3",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s3",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s6",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s6",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s7",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeRequest/s7",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeSendHeaders/s4",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeSendHeaders/s4",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeSendHeaders/s5",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onBeforeSendHeaders/s5",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onCompleted/s12",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onCompleted/s12",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onCompleted/s18",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onCompleted/s18",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onErrorOccurred/s13",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onErrorOccurred/s13",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s17",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s17",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s9",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s9",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onSendHeaders/s14",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onSendHeaders/s14",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onSendHeaders/s8",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "webRequest.onSendHeaders/s8",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onCreated",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onCreated",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onRemoved",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      }, {
         "event_name": "windows.onRemoved",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://ifinpabiejbjobcphhaomiifjibpkjlf/"
      } ]
   },
   "guid": "abc9f20b-8f2e-4995-91e0-a334c9c18094",
   "id": "ifinpabiejbjobcphhaomiifjibpkjlf",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Linewize Connect",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/ifinpabiejbjobcphhaomiifjibpkjlf/3.6.4_0",
   "permissions": {
      "active": {
         "api": [ "alarms", "cookies", "identity", "identity.email", "idle", "management", "storage", "tabs", "unlimitedStorage", "webNavigation", "webRequest", "webRequestBlocking", "enterprise.deviceAttributes", "scripting", "offscreen" ],
         "explicit_hosts": [ "\u003Call_urls>" ],
         "manifest": [  ],
         "scriptable_hosts": [ "*://*/*" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [ {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:264",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:257",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:275",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:274",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:286",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:284",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:256",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:289",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:256",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:283",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:261",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:253",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:275",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:248",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:266",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:240",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:264",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:254",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:273",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:272",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:287",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:295",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:282",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:270",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:239",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:247",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:248",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:290",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:233",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:263",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:279",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:253",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:265",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:295",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:276",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:257",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:271",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:260",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:278",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:254",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:267",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:236",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:235",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:249",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:283",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:290",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:289",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:287",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:268",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:246",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:291",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:247",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "63F0FB981FD31F14E5A3FC826D56566F:8",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:263",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:236",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:249",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:270",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:244",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:286",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:288",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:269",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:282",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:274",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:278",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:258",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:269",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:240",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:251",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:245",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:244",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:252",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:276",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:258",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:272",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:243",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:260",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:294",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:241",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:265",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:291",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:267",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:237",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:252",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:273",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:281",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:294",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:255",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:279",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:246",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:292",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:245",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:237",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:241",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:266",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:255",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "63F0FB981FD31F14E5A3FC826D56566F:8",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:259",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "E614D4ABB1020038A399A91EA7364099:4",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:284",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:271",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:239",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:268",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:243",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "E614D4ABB1020038A399A91EA7364099:4",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:251",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:261",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:281",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:235",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:259",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:292",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:233",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      }, {
         "extra_data": "132BAD958C3A41F5D815D74DB9138549:288",
         "timeout_type": "Default",
         "type": "MESSAGE_PORT"
      } ],
      "count": 112
   },
   "type": "TYPE_EXTENSION",
   "version": "3.6.4"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 2,
      "listeners": [ {
         "event_name": "action.onClicked",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://inomeogfingihgjfjlpeplalcfajhgai/"
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://inomeogfingihgjfjlpeplalcfajhgai/"
      } ]
   },
   "guid": "fe2cd14b-eab1-49a6-a570-fda71b82e87c",
   "id": "inomeogfingihgjfjlpeplalcfajhgai",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Chrome Remote Desktop",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/inomeogfingihgjfjlpeplalcfajhgai/2.1_0",
   "permissions": {
      "active": {
         "api": [ "downloads", "nativeMessaging" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "2.1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 14,
      "listeners": [ {
         "event_name": "alarms.onAlarm",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "alarms.onAlarm",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "runtime.onSuspend",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "runtime.onSuspend",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s3",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onBeforeRedirect/s3",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onCompleted/s2",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onCompleted/s2",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s1",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      }, {
         "event_name": "webRequest.onHeadersReceived/s1",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/"
      } ]
   },
   "guid": "0ca55874-2f3f-48b3-80fe-2167314e32c7",
   "id": "jfbecfmiegcjddenjhlbhlikcbfmnafd",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Securly Classroom",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/jfbecfmiegcjddenjhlbhlikcbfmnafd/1.34.2_0",
   "permissions": {
      "active": {
         "api": [ "activeTab", "alarms", "gcm", "geolocation", "identity", "identity.email", "idle", "nativeMessaging", "notifications", "storage", "webRequest", "enterprise.deviceAttributes", "declarativeNetRequest", "scripting", "declarativeNetRequestWithHostAccess", "offscreen" ],
         "explicit_hosts": [ "*://*/*", "\u003Call_urls>" ],
         "manifest": [  ],
         "scriptable_hosts": [ "\u003Call_urls>" ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.34.2"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 14,
      "listeners": [ {
         "event_name": "input.ime.onActivate",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onBlur",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onCandidateClicked",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onDeactivated",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onMenuItemActivated",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onReset",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "input.ime.onSurroundingTextChanged",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "inputMethodPrivate.onFocus",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "inputMethodPrivate.onScreenProjectionChanged",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "inputMethodPrivate.onSuggestionsChanged",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "system.display.onDisplayChanged",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "types.ChromeSetting.spokenFeedback.onChange",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "virtualKeyboardPrivate.onKeyboardClosed",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "virtualKeyboardPrivate.onKeyboardConfigChanged",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "2b9d22bc-17e1-44e9-97d2-6b6ae8dc6a5a",
   "id": "jkghodnilhceideoidjikpgommlajknk",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Chrome OS XKB",
   "path": "/usr/share/chromeos-assets/input_methods/input_tools",
   "permissions": {
      "active": {
         "api": [ "accessibilityFeatures.read", "app.window.alpha", "audioCapture", "app.window.ime", "input", "inputMethodPrivate", "metricsPrivate", "notifications", "system.display", "tabs", "tts", "unlimitedStorage", "virtualKeyboardPrivate" ],
         "explicit_hosts": [ "https://clients4.google.com/*", "https://dl.google.com/*", "https://handwriting.googleapis.com/*", "https://www.googleapis.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.0.5.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 21,
      "listeners": [ {
         "event_name": "cookies.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "cookies.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "permissions.onAdded",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "permissions.onAdded",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "permissions.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "permissions.onRemoved",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "runtime.onUpdateAvailable",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "storage.onChanged",
         "is_for_service_worker": false,
         "is_lazy": false,
         "url": ""
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "tabs.onActivated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "tabs.onUpdated",
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "windows.onFocusChanged",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "windows.onRemoved",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": true,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      }, {
         "event_name": "windows.onRemoved",
         "filter": {
         },
         "is_for_service_worker": true,
         "is_lazy": false,
         "url": "chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/"
      } ]
   },
   "guid": "6dde8590-c534-452d-b654-b2c49047ad8f",
   "id": "kbfnbcaeplbcioakkpcpgfkobkghlhen",
   "location": "EXTERNAL_POLICY_DOWNLOAD",
   "manifest_version": 3,
   "name": "Grammarly: AI Writing Assistant and Grammar Checker App",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/kbfnbcaeplbcioakkpcpgfkobkghlhen/14.1250.0_0",
   "permissions": {
      "active": {
         "api": [ "cookies", "identity", "notifications", "storage", "tabs", "scripting", "sidePanel" ],
         "explicit_hosts": [ "http://*/*", "https://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [ "*://*.apclassroom.collegeboard.org/*", "*://*.app.nearpod.com/*", "*://*.app.seesaw.me/*", "*://*.atlassian.net/*", "*://*.blackboard.com/*", "*://*.blogger.com/*", "*://*.calendar.google.com/*", "*://*.chat.google.com/*", "*://*.classroom.google.com/*", "*://*.commonlit.org/*", "*://*.coursera.org/*", "*://*.educationperfect.com/*", "*://*.facebook.com/*", "*://*.fiverr.com/*", "*://*.forms.office.com/*", "*://*.github.com/*", "*://*.intercom.io/*", "*://*.keep.google.com/*", "*://*.lightning.force.com/*", "*://*.linkedin.com/*", "*://*.mail.aol.com/*", "*://*.mail.google.com/*", "*://*.medium.com/*", "*://*.messenger.com/*", "*://*.onlinechatdashboard.com/*", "*://*.outlook.live.com/*", "*://*.outlook.office.com/*", "*://*.papago.naver.com/*", "*://*.publish.buffer.com/*", "*://*.quora.com/*", "*://*.readworks.org/*", "*://*.reddit.com/*", "*://*.slack.com/*", "*://*.studio.youtube.com/*", "*://*.teams.microsoft.com/*", "*://*.translate.google.com/*", "*://*.trello.com/*", "*://*.twitch.tv/*", "*://*.twitter.com/*", "*://*.upwork.com/*", "*://*.wattpad.com/*", "*://*.web.whatsapp.com/*", "*://*.wix.com/*", "*://*.wordcounter.net/*", "*://*.wordpress.com/*", "*://*.x.com/*", "*://*.youtube.com/*", "*://*.zendesk.com/*", "*://apclassroom.collegeboard.org/*", "*://app.nearpod.com/*", "*://app.seesaw.me/*", "*://calendar.google.com/*", "*://chat.google.com/*", "*://classroom.google.com/*", "*://commonlit.org/*", "*://coursera.org/*", "*://docs.google.com/*", "*://docs.google.com/document/*", "*://educationperfect.com/*", "*://facebook.com/*", "*://fiverr.com/*", "*://forms.office.com/*", "*://github.com/*", "*://intercom.io/*", "*://keep.google.com/*", "*://linkedin.com/*", "*://mail.aol.com/*", "*://mail.google.com/*", "*://medium.com/*", "*://messenger.com/*", "*://onlinechatdashboard.com/*", "*://outlook.live.com/*", "*://outlook.office.com/*", "*://papago.naver.com/*", "*://publish.buffer.com/*", "*://quora.com/*", "*://readworks.org/*", "*://reddit.com/*", "*://studio.youtube.com/*", "*://teams.microsoft.com/*", "*://translate.google.com/*", "*://trello.com/*", "*://twitch.tv/*", "*://twitter.com/*", "*://upwork.com/*", "*://wattpad.com/*", "*://web.whatsapp.com/*", "*://wix.com/*", "*://wordcounter.net/*", "*://wordpress.com/*", "*://x.com/*", "*://youtube.com/*", "\u003Call_urls>", "https://*.overleaf.com/*" ]
      },
      "optional": {
         "api": [ "clipboardRead", "nativeMessaging" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "14.1250.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "d6596195-0e8f-488b-b176-1717dfb40621",
   "id": "kddnkjkcjddckihglkfcickdhbmaodcn",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Chrome Goodies",
   "path": "/usr/share/chromeos-assets/echo",
   "permissions": {
      "active": {
         "api": [ "alarms", "chromeosInfoPrivate", "cookies", "echoPrivate", "metricsPrivate", "notifications", "storage" ],
         "explicit_hosts": [ "https://*/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.0.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "506368bf-a918-41a4-a6ba-430d9e0a0922",
   "id": "mgndgikekgjfcpckkfioiadnlibdjbkf",
   "location": "COMPONENT",
   "manifest_version": 1,
   "name": "Chrome",
   "path": "/opt/google/chrome/resources/chrome_app",
   "permissions": {
      "active": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_HOSTED_APP",
   "version": "0.1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "779102d4-c360-4a4b-a6d0-2e014ab6e316",
   "id": "mhjfbmdgcfjbbpaeojofohoefgiehjai",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Chrome PDF Viewer",
   "path": "/opt/google/chrome/resources/pdf",
   "permissions": {
      "active": {
         "api": [ "contentSettings", "fileSystem", "fileSystem.write", "metricsPrivate", "tabs", "resourcesPrivate", "pdfViewerPrivate" ],
         "explicit_hosts": [ "chrome://resources/*", "chrome://webui-test/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": -1
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 0,
      "listeners": [  ]
   },
   "guid": "79edb9d5-a189-4c6b-82b7-a459b88f389a",
   "id": "mppnpdlheglhdfmldimlhpnegondlapf",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "__MSG_chos_inputtool_title__",
   "path": "/opt/google/chrome/resources/keyboard",
   "permissions": {
      "active": {
         "api": [ "inputMethodPrivate", "tabs", "virtualKeyboardPrivate" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.0.6.0"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 1,
      "listeners": [ {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "1314ba8f-682c-4029-bf71-f3279ec6e0e6",
   "id": "nkeimhogjdpnpccoofpliimaahmaaome",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Google Hangouts",
   "path": "/opt/google/chrome/resources/hangout_services",
   "permissions": {
      "active": {
         "api": [ "desktopCapture", "processes", "webrtcDesktopCapturePrivate", "webrtcLoggingPrivate", "system.cpu", "enterprise.hardwarePlatform" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "1.3.21"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY", "FROM_WEBSTORE", "WAS_INSTALLED_BY_DEFAULT" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 2,
      "listeners": [ {
         "event_name": "app.runtime.onLaunched",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      }, {
         "event_name": "runtime.onConnectExternal",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "c026b155-253a-402e-80df-41f7c5e6b51f",
   "id": "nmmhkkegccagdldgiimedpiccmgmieda",
   "location": "EXTERNAL_COMPONENT",
   "manifest_version": 2,
   "name": "Chrome Web Store Payments",
   "path": "/home/chronos/u-b46af3ebcc948f3ab7717e630982a60afaf9e9b9/Extensions/nmmhkkegccagdldgiimedpiccmgmieda/1.0.0.6_0",
   "permissions": {
      "active": {
         "api": [ "identity", "webview" ],
         "explicit_hosts": [ "https://payments.google.com/*", "https://sandbox.google.com/*", "https://www.google.com/*", "https://www.googleapis.com/*" ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_PLATFORM_APP",
   "version": "1.0.0.6"
}, {
   "background_page_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "creation_flags": [ "REQUIRE_KEY" ],
   "disable_reasons": [  ],
   "event_listeners": {
      "count": 1,
      "listeners": [ {
         "event_name": "runtime.onConnectNative",
         "is_for_service_worker": false,
         "is_lazy": true,
         "url": ""
      } ]
   },
   "guid": "03aade03-625c-4689-ac27-db21be32496b",
   "id": "pmfjbimdmchhbnneeidfognadeopoehp",
   "location": "COMPONENT",
   "manifest_version": 2,
   "name": "Image loader",
   "path": "/opt/google/chrome/resources/image_loader",
   "permissions": {
      "active": {
         "api": [ "nativeMessaging", "imageLoaderPrivate" ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "optional": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      },
      "tab_specific": {
      },
      "withheld": {
         "api": [  ],
         "explicit_hosts": [  ],
         "manifest": [  ],
         "scriptable_hosts": [  ]
      }
   },
   "service_worker_keepalives": {
      "activites": [  ],
      "count": 0
   },
   "type": "TYPE_EXTENSION",
   "version": "0.2"
} ]
