import random
import time
import hashlib
import base64
from playwright.async_api import Page

class AdvancedBrowserAutomation:
    """
    Advanced browser automation system for legitimate web testing and automation tasks.
    Provides realistic browser profiles and human-like behavior patterns.
    """

    @staticmethod
    def get_realistic_user_agents():
        """
        Returns realistic and up-to-date user agents with intelligent rotation.
        Uses current browser versions from 2024/2025.
        """
        user_agents = [
            # Modern Chrome - 2024/2025
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            
            # Modern Firefox with accurate version numbers
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
            
            # Modern Edge synchronized with Chrome
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            
            # Modern Safari
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
        ]
        
        # Add variation to build numbers
        selected = random.choice(user_agents)
        if "Chrome/" in selected:
            import re
            selected = re.sub(r'Chrome/(\d+)\.(\d+)\.(\d+)\.(\d+)', 
                            lambda m: f"Chrome/{m.group(1)}.{m.group(2)}.{m.group(3)}.{random.randint(0, 999)}", 
                            selected)
        
        return selected

    @staticmethod
    def get_realistic_screen_configs():
        """
        Returns realistic screen configurations with advanced pixel ratios.
        Based on common display resolutions.
        """
        configs = [
            # Common resolutions
            {"width": 1920, "height": 1080, "device_pixel_ratio": 1.0, "color_depth": 24},
            {"width": 1366, "height": 768, "device_pixel_ratio": 1.0, "color_depth": 24},
            {"width": 1440, "height": 900, "device_pixel_ratio": 1.0, "color_depth": 24},
            {"width": 1536, "height": 864, "device_pixel_ratio": 1.25, "color_depth": 24},
            {"width": 1280, "height": 720, "device_pixel_ratio": 1.0, "color_depth": 24},
            
            # High resolution displays
            {"width": 2560, "height": 1440, "device_pixel_ratio": 1.0, "color_depth": 30},
            {"width": 3840, "height": 2160, "device_pixel_ratio": 1.0, "color_depth": 30},
            {"width": 2560, "height": 1600, "device_pixel_ratio": 1.0, "color_depth": 24},
            
            # MacBook displays
            {"width": 1680, "height": 1050, "device_pixel_ratio": 2.0, "color_depth": 30},
            {"width": 1440, "height": 900, "device_pixel_ratio": 2.0, "color_depth": 30},
        ]
        
        selected = random.choice(configs)
        # Add slight variation to dimensions
        selected["width"] += random.randint(-2, 2)
        selected["height"] += random.randint(-2, 2)
        
        return selected

    @staticmethod
    async def inject_browser_enhancements(page: Page):
        """
        Injects browser enhancements for realistic automation behavior.
        Provides consistent browser profiles and prevents detection anomalies.
        """
        
        # Part 1: Basic browser property management
        enhancement_part_1 = """
        (() => {
            'use strict';
            
            console.log('🔧 Browser Enhancement System v3.0 - Initializing...');
            
            // ===== 1. Remove automation properties =====
            
            // List of known automation properties
            const automationProperties = [
                'webdriver', '__webdriver_script_fn', '__webdriver_evaluate', '__selenium_unwrapped',
                '__selenium_evaluate', '__webdriver_unwrapped', '__driver_evaluate', '__webdriver_script_func',
                '__webdriver_script_function', '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_active',
                '__webdriver_chrome_runtime', '__nightmare', 'phantom', '_phantom', '__phantom',
                'callPhantom', '_selenium', 'calledSelenium', '$chrome_asyncScriptInfo', '__$webdriverAsyncExecutor',
                'webdriverCommand', '__playwright', '_playwright', 'playwright', '__pwInitScripts',
                '__cdp_runtime_evaluate', '__runtime_evaluate', 'domAutomation', 'domAutomationController',
                '__chrome_devtools_api', '__webdriver_chrome_runtime', 'fmget_targets', '_WEBDRIVER_ELEM_CACHE'
            ];
            
            // Remove all properties from window and navigator
            automationProperties.forEach(prop => {
                try {
                    delete window[prop];
                    delete navigator[prop];
                    delete document[prop];
                    
                    // Define property as undefined permanently
                    Object.defineProperty(window, prop, {
                        get: () => undefined,
                        set: () => {},
                        configurable: false,
                        enumerable: false
                    });
                    
                    Object.defineProperty(navigator, prop, {
                        get: () => undefined,
                        set: () => {},
                        configurable: false,
                        enumerable: false
                    });
                } catch (e) {}
            });
            
            // Special protection for webdriver
            Object.defineProperty(navigator, 'webdriver', {
                get: () => {
                    console.log('🔒 webdriver access attempt detected and blocked');
                    return undefined;
                },
                set: () => {},
                configurable: false,
                enumerable: false
            });
            
            // ===== 2. Realistic Navigator properties =====
            
            // Realistic plugin simulation
            const createRealisticPlugins = () => {
                const commonPlugins = [
                    {
                        name: 'PDF Viewer',
                        filename: 'internal-pdf-viewer',
                        description: 'Portable Document Format',
                        length: 2,
                        0: { type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: null },
                        1: { type: 'application/x-google-chrome-pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: null }
                    },
                    {
                        name: 'Chrome PDF Viewer',
                        filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai',
                        description: '',
                        length: 1,
                        0: { type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: null }
                    },
                    {
                        name: 'Chromium PDF Viewer',
                        filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai',
                        description: '',
                        length: 1,
                        0: { type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: null }
                    }
                ];
                
                // Add random realistic plugins
                const randomPlugins = [
                    { name: 'Widevine Content Decryption Module', filename: 'widevinecdmadapter.dll', description: 'Enables Widevine licenses for playback of HTML audio/video content.' },
                    { name: 'Google Update', filename: 'npGoogleUpdate3.dll', description: 'Google Update' },
                    { name: 'Microsoft Edge WebView2', filename: 'msedgewebview2.exe', description: 'Microsoft Edge WebView2' }
                ];
                
                const plugins = [...commonPlugins];
                
                if (Math.random() > 0.3) {
                    plugins.push(randomPlugins[Math.floor(Math.random() * randomPlugins.length)]);
                }
                
                plugins.refresh = function() { return undefined; };
                
                Object.defineProperty(plugins, 'length', {
                    get: () => plugins.filter(p => typeof p === 'object' && p.name).length,
                    configurable: false
                });
                
                return plugins;
            };
            
            Object.defineProperty(navigator, 'plugins', {
                get: () => createRealisticPlugins(),
                configurable: true
            });
            
            // Realistic mimeTypes
            const createRealisticMimeTypes = () => {
                const mimeTypes = [
                    { type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: { name: 'PDF Viewer' } },
                    { type: 'application/x-google-chrome-pdf', suffixes: 'pdf', description: 'Portable Document Format', enabledPlugin: { name: 'Chrome PDF Viewer' } },
                    { type: 'application/x-nacl', suffixes: '', description: 'Native Client Executable', enabledPlugin: { name: 'Native Client' } },
                    { type: 'application/x-pnacl', suffixes: '', description: 'Portable Native Client Executable', enabledPlugin: { name: 'Native Client' } }
                ];
                
                mimeTypes.namedItem = function(name) {
                    return this.find(mime => mime.type === name) || null;
                };
                
                return mimeTypes;
            };
            
            Object.defineProperty(navigator, 'mimeTypes', {
                get: () => createRealisticMimeTypes(),
                configurable: true
            });
            
            // Realistic language settings
            const languages = ['en-US', 'en'];
            if (Math.random() > 0.7) {
                languages.push('ar-SA', 'ar');
            }
            if (Math.random() > 0.8) {
                languages.push('es-ES', 'es');
            }
            
            Object.defineProperty(navigator, 'languages', {
                get: () => languages,
                configurable: true
            });
            
            Object.defineProperty(navigator, 'language', {
                get: () => languages[0],
                configurable: true
            });
            
            // ===== 3. Enhanced Chrome Runtime =====
            
            const createRealisticChromeRuntime = () => ({
                runtime: {
                    onConnect: {
                        addListener: () => {},
                        removeListener: () => {},
                        hasListener: () => false,
                        hasListeners: () => false
                    },
                    onMessage: {
                        addListener: () => {},
                        removeListener: () => {},
                        hasListener: () => false,
                        hasListeners: () => false
                    },
                    sendMessage: function() {
                        throw new Error('Could not establish connection. Receiving end does not exist.');
                    },
                    connect: function() {
                        throw new Error('Could not establish connection. Receiving end does not exist.');
                    },
                    onConnectExternal: undefined,
                    onMessageExternal: undefined,
                    id: undefined
                },
                
                loadTimes: function() {
                    const now = Date.now() / 1000;
                    return {
                        requestTime: now - Math.random() * 3,
                        startLoadTime: now - Math.random() * 2,
                        commitLoadTime: now - Math.random() * 1.5,
                        finishDocumentLoadTime: now - Math.random() * 1,
                        finishLoadTime: now - Math.random() * 0.5,
                        firstPaintTime: now - Math.random() * 0.8,
                        firstPaintAfterLoadTime: 0,
                        navigationType: 'Navigation',
                        wasFetchedViaSpdy: Math.random() > 0.5,
                        wasNpnNegotiated: Math.random() > 0.7,
                        npnNegotiatedProtocol: Math.random() > 0.5 ? 'h2' : 'http/1.1',
                        wasAlternateProtocolAvailable: Math.random() > 0.6,
                        connectionInfo: Math.random() > 0.3 ? 'h2' : 'http/1.1'
                    };
                },
                
                csi: function() {
                    const now = Date.now();
                    return {
                        onloadT: now,
                        pageT: now - Math.random() * 2000,
                        startE: now - Math.random() * 5000,
                        tran: Math.floor(Math.random() * 50) + 1
                    };
                },
                
                app: {
                    isInstalled: false,
                    getDetails: () => null,
                    getIsInstalled: () => false,
                    runningState: () => 'cannot_run'
                }
            });
            
            if (!window.chrome || Object.keys(window.chrome).length === 0) {
                Object.defineProperty(window, 'chrome', {
                    get: () => createRealisticChromeRuntime(),
                    configurable: true
                });
            }
        })();
        """
        
        # Part 2: Advanced API enhancements
        enhancement_part_2 = """
        (() => {
            'use strict';
            
            // ===== 4. Advanced Permissions API =====
            
            const originalPermissionsQuery = navigator.permissions.query;
            navigator.permissions.query = function(parameters) {
                const permissionStates = {
                    'notifications': Math.random() > 0.5 ? 'default' : 'denied',
                    'geolocation': Math.random() > 0.7 ? 'prompt' : 'denied',
                    'camera': Math.random() > 0.8 ? 'prompt' : 'denied',
                    'microphone': Math.random() > 0.8 ? 'prompt' : 'denied',
                    'midi': 'prompt',
                    'persistent-storage': 'prompt',
                    'accelerometer': 'granted',
                    'gyroscope': 'granted',
                    'magnetometer': 'granted',
                    'clipboard-read': 'prompt',
                    'clipboard-write': 'granted'
                };
                
                const state = permissionStates[parameters.name] || 'prompt';
                
                return Promise.resolve({
                    state: state,
                    addEventListener: function() {},
                    removeEventListener: function() {},
                    onchange: null
                });
            };
            
            // ===== 5. Canvas Fingerprint Protection =====
            
            const canvasProto = HTMLCanvasElement.prototype;
            const originalGetContext = canvasProto.getContext;
            const originalToDataURL = canvasProto.toDataURL;
            const originalToBlob = canvasProto.toBlob;
            
            // Create subtle noise system
            const createCanvasNoise = (data, width, height) => {
                const imageData = new Uint8ClampedArray(data);
                const len = imageData.length;
                
                const noisePattern = Math.random() * 0.01;
                const seed = (Date.now() % 1000) / 1000;
                
                for (let i = 0; i < len; i += 4) {
                    if (Math.random() < noisePattern) {
                        const noise = Math.sin(seed + i * 0.001) * 2;
                        imageData[i] = Math.max(0, Math.min(255, imageData[i] + noise));
                        imageData[i + 1] = Math.max(0, Math.min(255, imageData[i + 1] + noise));
                        imageData[i + 2] = Math.max(0, Math.min(255, imageData[i + 2] + noise));
                    }
                }
                
                return imageData;
            };
            
            canvasProto.getContext = function(contextType, ...args) {
                const context = originalGetContext.apply(this, [contextType, ...args]);
                
                if (context && contextType === '2d') {
                    const originalGetImageData = context.getImageData;
                    const originalFillText = context.fillText;
                    const originalStrokeText = context.strokeText;
                    const originalArc = context.arc;
                    const originalFillRect = context.fillRect;
                    
                    // Add subtle variations to text rendering
                    context.fillText = function(...args) {
                        const noise = (Math.random() - 0.5) * 0.002;
                        if (args.length >= 3) {
                            args[1] += noise;
                            args[2] += noise;
                        }
                        return originalFillText.apply(this, args);
                    };
                    
                    context.strokeText = function(...args) {
                        const noise = (Math.random() - 0.5) * 0.002;
                        if (args.length >= 3) {
                            args[1] += noise;
                            args[2] += noise;
                        }
                        return originalStrokeText.apply(this, args);
                    };
                    
                    // Add subtle variations to shapes
                    context.arc = function(...args) {
                        if (args.length >= 3) {
                            args[2] += (Math.random() - 0.5) * 0.001;
                        }
                        return originalArc.apply(this, args);
                    };
                    
                    context.fillRect = function(...args) {
                        const noise = (Math.random() - 0.5) * 0.001;
                        if (args.length >= 4) {
                            args[0] += noise;
                            args[1] += noise;
                        }
                        return originalFillRect.apply(this, args);
                    };
                    
                    // Add subtle noise to image data
                    context.getImageData = function(...args) {
                        const imageData = originalGetImageData.apply(this, args);
                        const noisyData = createCanvasNoise(imageData.data, imageData.width, imageData.height);
                        return new ImageData(noisyData, imageData.width, imageData.height);
                    };
                }
                
                return context;
            };
            
            // Add subtle variation to toDataURL
            canvasProto.toDataURL = function(...args) {
                const context = this.getContext('2d');
                if (context) {
                    const originalData = context.getImageData(0, 0, this.width, this.height);
                    const x = Math.floor(Math.random() * this.width);
                    const y = Math.floor(Math.random() * this.height);
                    const noise = Math.floor(Math.random() * 3) - 1;
                    
                    context.fillStyle = `rgba(${noise},${noise},${noise},0.01)`;
                    context.fillRect(x, y, 1, 1);
                    
                    const result = originalToDataURL.apply(this, args);
                    
                    context.putImageData(originalData, 0, 0);
                    
                    return result;
                }
                return originalToDataURL.apply(this, args);
            };
            
            // ===== 6. WebGL Fingerprint Protection =====
            
            const getContext = HTMLCanvasElement.prototype.getContext;
            HTMLCanvasElement.prototype.getContext = function(contextType, ...args) {
                const context = getContext.apply(this, [contextType, ...args]);
                
                if (context && (contextType.includes('webgl') || contextType.includes('experimental-webgl'))) {
                    const originalGetParameter = context.getParameter;
                    const originalGetExtension = context.getExtension;
                    const originalGetShaderPrecisionFormat = context.getShaderPrecisionFormat;
                    
                    // Realistic GPU list
                    const realisticGPUs = [
                        'ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)',
                        'ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.5671)',
                        'ANGLE (AMD, AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)',
                        'ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)',
                        'ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.9649)'
                    ];
                    
                    const selectedGPU = realisticGPUs[Math.floor(Math.random() * realisticGPUs.length)];
                    
                    const fakeParameters = {
                        [context.VENDOR]: 'Google Inc. (Intel)',
                        [context.RENDERER]: selectedGPU,
                        [context.VERSION]: 'WebGL 1.0 (OpenGL ES 2.0 Chromium)',
                        [context.SHADING_LANGUAGE_VERSION]: 'WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)',
                        [context.UNMASKED_VENDOR_WEBGL]: 'Google Inc. (Intel)',
                        [context.UNMASKED_RENDERER_WEBGL]: selectedGPU,
                        [context.MAX_VIEWPORT_DIMS]: new Int32Array([16384, 16384]),
                        [context.MAX_TEXTURE_SIZE]: 16384,
                        [context.MAX_CUBE_MAP_TEXTURE_SIZE]: 16384,
                        [context.MAX_RENDERBUFFER_SIZE]: 16384,
                        [context.MAX_TEXTURE_IMAGE_UNITS]: 16,
                        [context.MAX_VERTEX_TEXTURE_IMAGE_UNITS]: 16,
                        [context.MAX_COMBINED_TEXTURE_IMAGE_UNITS]: 32,
                        [context.MAX_VERTEX_ATTRIBS]: 16,
                        [context.MAX_VARYING_VECTORS]: 15,
                        [context.MAX_VERTEX_UNIFORM_VECTORS]: 1024,
                        [context.MAX_FRAGMENT_UNIFORM_VECTORS]: 1024,
                        [context.ALIASED_LINE_WIDTH_RANGE]: new Float32Array([1, 1]),
                        [context.ALIASED_POINT_SIZE_RANGE]: new Float32Array([1, 1024])
                    };
                    
                    context.getParameter = function(parameter) {
                        if (parameter in fakeParameters) {
                            return fakeParameters[parameter];
                        }
                        return originalGetParameter.apply(this, arguments);
                    };
                    
                    // Realistic extension simulation
                    const allowedExtensions = [
                        'ANGLE_instanced_arrays', 'EXT_blend_minmax', 'EXT_color_buffer_half_float',
                        'EXT_disjoint_timer_query', 'EXT_frag_depth', 'EXT_shader_texture_lod',
                        'EXT_texture_filter_anisotropic', 'WEBKIT_EXT_texture_filter_anisotropic',
                        'EXT_sRGB', 'OES_element_index_uint', 'OES_standard_derivatives',
                        'OES_texture_float', 'OES_texture_half_float', 'OES_vertex_array_object',
                        'WEBGL_color_buffer_float', 'WEBGL_compressed_texture_s3tc',
                        'WEBKIT_WEBGL_compressed_texture_s3tc', 'WEBGL_debug_renderer_info',
                        'WEBGL_debug_shaders', 'WEBGL_depth_texture', 'WEBKIT_WEBGL_depth_texture',
                        'WEBGL_draw_buffers', 'WEBGL_lose_context', 'WEBKIT_WEBGL_lose_context'
                    ];
                    
                    const availableExtensions = allowedExtensions.filter(() => Math.random() > 0.3);
                    
                    context.getExtension = function(name) {
                        if (availableExtensions.includes(name)) {
                            return originalGetExtension.apply(this, arguments) || {};
                        }
                        return null;
                    };
                    
                    context.getSupportedExtensions = function() {
                        return availableExtensions;
                    };
                    
                    // Add variation to shader precision
                    context.getShaderPrecisionFormat = function(shaderType, precisionType) {
                        const result = originalGetShaderPrecisionFormat.apply(this, arguments);
                        if (result) {
                            return {
                                rangeMin: result.rangeMin + Math.floor(Math.random() * 3) - 1,
                                rangeMax: result.rangeMax + Math.floor(Math.random() * 3) - 1,
                                precision: result.precision + Math.floor(Math.random() * 3) - 1
                            };
                        }
                        return result;
                    };
                }
                
                return context;
            };
        })();
        """
        
        # Part 3: Advanced tracking protection
        enhancement_part_3 = """
        (() => {
            'use strict';
            
            // ===== 7. AudioContext Fingerprint Protection =====
            
            if (window.AudioContext || window.webkitAudioContext) {
                const OriginalAudioContext = window.AudioContext || window.webkitAudioContext;
                
                const AudioContextWrapper = function(...args) {
                    const context = new OriginalAudioContext(...args);
                    
                    const originalCreateOscillator = context.createOscillator;
                    const originalCreateAnalyser = context.createAnalyser;
                    
                    Object.defineProperty(context, 'sampleRate', {
                        get: () => {
                            const rates = [44100, 48000, 96000];
                            const baseRate = rates[Math.floor(Math.random() * rates.length)];
                            return baseRate + (Math.random() * 100 - 50);
                        },
                        configurable: true
                    });
                    
                    Object.defineProperty(context, 'baseLatency', {
                        get: () => Math.random() * 0.01 + 0.005,
                        configurable: true
                    });
                    
                    context.createOscillator = function() {
                        const oscillator = originalCreateOscillator.apply(this, arguments);
                        const originalStart = oscillator.start;
                        
                        oscillator.start = function(when = 0) {
                            return originalStart.call(this, when + Math.random() * 0.001);
                        };
                        
                        return oscillator;
                    };
                    
                    context.createAnalyser = function() {
                        const analyser = originalCreateAnalyser.apply(this, arguments);
                        const originalGetFloatFrequencyData = analyser.getFloatFrequencyData;
                        
                        analyser.getFloatFrequencyData = function(array) {
                            originalGetFloatFrequencyData.call(this, array);
                            for (let i = 0; i < array.length; i++) {
                                array[i] += (Math.random() - 0.5) * 0.1;
                            }
                        };
                        
                        return analyser;
                    };
                    
                    return context;
                };
                
                AudioContextWrapper.prototype = OriginalAudioContext.prototype;
                window.AudioContext = AudioContextWrapper;
                if (window.webkitAudioContext) {
                    window.webkitAudioContext = AudioContextWrapper;
                }
            }
            
            // ===== 8. Enhanced device properties =====
            
            Object.defineProperty(navigator, 'hardwareConcurrency', {
                get: () => {
                    const cores = [2, 4, 6, 8, 12, 16];
                    return cores[Math.floor(Math.random() * cores.length)];
                },
                configurable: true
            });
            
            Object.defineProperty(navigator, 'deviceMemory', {
                get: () => {
                    const memory = [2, 4, 8, 16, 32];
                    return memory[Math.floor(Math.random() * memory.length)];
                },
                configurable: true
            });
            
            Object.defineProperty(navigator, 'maxTouchPoints', {
                get: () => Math.random() > 0.8 ? Math.floor(Math.random() * 10) + 1 : 0,
                configurable: true
            });
            
            // ===== 9. Event handling enhancement =====
            
            const originalAddEventListener = EventTarget.prototype.addEventListener;
            const originalRemoveEventListener = EventTarget.prototype.removeEventListener;
            
            const eventListeners = new WeakMap();
            
            EventTarget.prototype.addEventListener = function(type, listener, options) {
                const humanEvents = ['click', 'mousedown', 'mouseup', 'mousemove', 'keydown', 'keyup', 'scroll'];
                
                if (humanEvents.includes(type)) {
                    const wrappedListener = function(event) {
                        Object.defineProperty(event, 'isTrusted', {
                            get: () => true,
                            configurable: true
                        });
                        
                        if (type.startsWith('mouse')) {
                            Object.defineProperty(event, 'movementX', {
                                get: () => Math.floor(Math.random() * 3) - 1,
                                configurable: true
                            });
                            Object.defineProperty(event, 'movementY', {
                                get: () => Math.floor(Math.random() * 3) - 1,
                                configurable: true
                            });
                        }
                        
                        const delay = Math.random() * 3 + 1;
                        setTimeout(() => {
                            if (typeof listener === 'function') {
                                listener.call(this, event);
                            } else if (listener && typeof listener.handleEvent === 'function') {
                                listener.handleEvent.call(listener, event);
                            }
                        }, delay);
                    };
                    
                    if (!eventListeners.has(this)) {
                        eventListeners.set(this, new Map());
                    }
                    eventListeners.get(this).set(listener, wrappedListener);
                    
                    return originalAddEventListener.call(this, type, wrappedListener, options);
                }
                
                return originalAddEventListener.call(this, type, listener, options);
            };
            
            EventTarget.prototype.removeEventListener = function(type, listener, options) {
                if (eventListeners.has(this) && eventListeners.get(this).has(listener)) {
                    const wrappedListener = eventListeners.get(this).get(listener);
                    eventListeners.get(this).delete(listener);
                    return originalRemoveEventListener.call(this, type, wrappedListener, options);
                }
                
                return originalRemoveEventListener.call(this, type, listener, options);
            };
            
            // ===== 10. Timing API protection =====
            
            const originalPerformanceNow = Performance.prototype.now;
            const timeOffset = Math.random() * 100;
            
            Performance.prototype.now = function() {
                const realTime = originalPerformanceNow.apply(this, arguments);
                return realTime + timeOffset + (Math.random() - 0.5) * 0.1;
            };
            
            const originalDateNow = Date.now;
            Date.now = function() {
                return originalDateNow() + Math.floor(Math.random() * 3) - 1;
            };
            
            const originalGetTime = Date.prototype.getTime;
            Date.prototype.getTime = function() {
                return originalGetTime.call(this) + Math.floor(Math.random() * 3) - 1;
            };
            
            // ===== 11. Battery API protection =====
            
            if (navigator.getBattery) {
                navigator.getBattery = () => Promise.resolve({
                    charging: Math.random() > 0.4,
                    chargingTime: Math.random() > 0.5 ? Infinity : Math.random() * 14400,
                    dischargingTime: Math.random() * 28800 + 3600,
                    level: Math.random() * 0.7 + 0.2,
                    addEventListener: () => {},
                    removeEventListener: () => {},
                    onchargingchange: null,
                    onchargingtimechange: null,
                    ondischargingtimechange: null,
                    onlevelchange: null
                });
            }
            
            Object.defineProperty(navigator, 'battery', {
                get: () => undefined,
                configurable: true
            });
            
            // ===== 12. Connection API enhancement =====
            
            const createRealisticConnection = () => ({
                downlink: parseFloat((Math.random() * 9 + 1).toFixed(1)),
                effectiveType: ['slow-2g', '2g', '3g', '4g'][Math.floor(Math.random() * 4)],
                rtt: Math.floor(Math.random() * 150) + 50,
                saveData: Math.random() > 0.9,
                type: ['bluetooth', 'cellular', 'ethernet', 'wifi', 'wimax', 'other', 'unknown'][Math.floor(Math.random() * 7)],
                addEventListener: () => {},
                removeEventListener: () => {},
                onchange: null
            });
            
            if (navigator.connection) {
                Object.defineProperty(navigator, 'connection', {
                    get: () => createRealisticConnection(),
                    configurable: true
                });
            }
            
            // ===== 13. Screen fingerprint protection =====
            
            const originalScreen = window.screen;
            const screenConfig = {
                width: originalScreen.width + Math.floor(Math.random() * 3) - 1,
                height: originalScreen.height + Math.floor(Math.random() * 3) - 1,
                availWidth: originalScreen.availWidth + Math.floor(Math.random() * 3) - 1,
                availHeight: originalScreen.availHeight + Math.floor(Math.random() * 3) - 1,
                colorDepth: [24, 30, 32][Math.floor(Math.random() * 3)],
                pixelDepth: [24, 30, 32][Math.floor(Math.random() * 3)]
            };
            
            Object.keys(screenConfig).forEach(key => {
                Object.defineProperty(screen, key, {
                    get: () => screenConfig[key],
                    configurable: true
                });
            });
            
            // ===== 14. Timezone detection protection =====
            
            const originalGetTimezoneOffset = Date.prototype.getTimezoneOffset;
            Date.prototype.getTimezoneOffset = function() {
                const original = originalGetTimezoneOffset.call(this);
                return original + Math.floor(Math.random() * 3) - 1;
            };
            
            const originalResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
            Intl.DateTimeFormat.prototype.resolvedOptions = function() {
                const options = originalResolvedOptions.call(this);
                const timezones = [
                    'America/New_York', 'Europe/London', 'Asia/Tokyo', 
                    'America/Los_Angeles', 'Europe/Paris', 'Asia/Shanghai'
                ];
                
                return {
                    ...options,
                    timeZone: timezones[Math.floor(Math.random() * timezones.length)]
                };
            };
            
            // ===== 15. Font detection protection =====
            
            const originalOffsetWidth = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetWidth');
            const originalOffsetHeight = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');
            
            if (originalOffsetWidth) {
                Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {
                    get: function() {
                        const width = originalOffsetWidth.get.call(this);
                        return width + (Math.random() > 0.95 ? Math.floor(Math.random() * 3) - 1 : 0);
                    },
                    configurable: true
                });
            }
            
            if (originalOffsetHeight) {
                Object.defineProperty(HTMLElement.prototype, 'offsetHeight', {
                    get: function() {
                        const height = originalOffsetHeight.get.call(this);
                        return height + (Math.random() > 0.95 ? Math.floor(Math.random() * 3) - 1 : 0);
                    },
                    configurable: true
                });
            }
            
            // ===== 16. iframe detection protection =====
            
            Object.defineProperty(window, 'top', {
                get: () => window,
                configurable: false
            });
            
            Object.defineProperty(window, 'parent', {
                get: () => window,
                configurable: false
            });
            
            Object.defineProperty(window, 'frameElement', {
                get: () => null,
                configurable: false
            });
            
            // ===== 17. Document properties enhancement =====
            
            const documentProperties = ['hidden', 'visibilityState', 'webkitHidden', 'webkitVisibilityState'];
            
            documentProperties.forEach(prop => {
                if (prop.includes('hidden')) {
                    Object.defineProperty(document, prop, {
                        get: () => false,
                        configurable: true
                    });
                } else if (prop.includes('visibilityState')) {
                    Object.defineProperty(document, prop, {
                        get: () => 'visible',
                        configurable: true
                    });
                }
            });
            
            // ===== 18. Speech API enhancement =====
            
            if (window.speechSynthesis) {
                const originalGetVoices = window.speechSynthesis.getVoices;
                window.speechSynthesis.getVoices = function() {
                    const voices = originalGetVoices.call(this);
                    return voices.slice(0, Math.floor(Math.random() * 5) + 3);
                };
            }
            
            if (window.SpeechSynthesisUtterance) {
                const original = window.SpeechSynthesisUtterance.prototype.constructor;
                window.SpeechSynthesisUtterance = function(...args) {
                    const utterance = new original(...args);
                    utterance.rate = 1 + (Math.random() - 0.5) * 0.2;
                    utterance.pitch = 1 + (Math.random() - 0.5) * 0.2;
                    return utterance;
                };
            }
            
            console.log('🔧 Part 2/3 - Advanced API Protection Loaded');
        })();
        """
        
        # Part 4: Final protection layer and behavior simulation
        enhancement_part_4 = """
        (() => {
            'use strict';
            
            // ===== 19. Network fingerprint protection =====
            
            const originalFetch = window.fetch;
            window.fetch = function(input, init = {}) {
                const headers = new Headers(init.headers || {});
                
                const realisticHeaders = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Cache-Control': ['no-cache', 'max-age=0', 'no-store'][Math.floor(Math.random() * 3)],
                    'Pragma': Math.random() > 0.5 ? 'no-cache' : undefined,
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'DNT': Math.random() > 0.7 ? '1' : undefined
                };
                
                Object.entries(realisticHeaders).forEach(([key, value]) => {
                    if (value && !headers.has(key)) {
                        headers.set(key, value);
                    }
                });
                
                init.headers = headers;
                
                const delay = Math.random() * 100 + 50;
                
                return new Promise(resolve => {
                    setTimeout(() => {
                        resolve(originalFetch(input, init));
                    }, delay);
                });
            };
            
            // XMLHttpRequest enhancement
            const originalXHROpen = XMLHttpRequest.prototype.open;
            const originalXHRSend = XMLHttpRequest.prototype.send;
            
            XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
                this._method = method;
                this._url = url;
                return originalXHROpen.apply(this, arguments);
            };
            
            XMLHttpRequest.prototype.send = function(data) {
                const delay = Math.random() * 50 + 20;
                setTimeout(() => {
                    originalXHRSend.call(this, data);
                }, delay);
            };
            
            // ===== 20. CSS Media Queries protection =====
            
            const originalMatchMedia = window.matchMedia;
            window.matchMedia = function(query) {
                const result = originalMatchMedia.call(this, query);
                
                if (query.includes('hover') || query.includes('pointer')) {
                    return {
                        matches: Math.random() > 0.3,
                        media: query,
                        addListener: () => {},
                        removeListener: () => {},
                        addEventListener: () => {},
                        removeEventListener: () => {},
                        dispatchEvent: () => true
                    };
                }
                
                return result;
            };
            
            // ===== 21. Gamepad API protection =====
            
            if (navigator.getGamepads) {
                navigator.getGamepads = () => {
                    return Math.random() > 0.9 ? [null, null, null, null] : [];
                };
            }
            
            Object.defineProperty(navigator, 'gamepads', {
                get: () => [],
                configurable: true
            });
            
            // ===== 22. USB/Serial APIs protection =====
            
            if (navigator.usb) {
                Object.defineProperty(navigator, 'usb', {
                    get: () => ({
                        getDevices: () => Promise.resolve([]),
                        requestDevice: () => Promise.reject(new DOMException('Access denied', 'NotAllowedError')),
                        addEventListener: () => {},
                        removeEventListener: () => {}
                    }),
                    configurable: true
                });
            }
            
            if (navigator.serial) {
                Object.defineProperty(navigator, 'serial', {
                    get: () => ({
                        getPorts: () => Promise.resolve([]),
                        requestPort: () => Promise.reject(new DOMException('Access denied', 'NotAllowedError')),
                        addEventListener: () => {},
                        removeEventListener: () => {}
                    }),
                    configurable: true
                });
            }
            
            // ===== 23. WebRTC fingerprint protection =====
            
            if (window.RTCPeerConnection) {
                const originalRTCPeerConnection = window.RTCPeerConnection;
                window.RTCPeerConnection = function(configuration, constraints) {
                    if (configuration && configuration.iceServers) {
                        configuration.iceServers = configuration.iceServers.filter(
                            server => !server.urls || !server.urls.toString().includes('stun')
                        );
                    }
                    
                    const pc = new originalRTCPeerConnection(configuration, constraints);
                    
                    const originalGetStats = pc.getStats;
                    pc.getStats = function(...args) {
                        return originalGetStats.apply(this, args).then(stats => {
                            stats.forEach(stat => {
                                if (stat.type === 'local-candidate' || stat.type === 'remote-candidate') {
                                    stat.ip = '192.168.1.' + Math.floor(Math.random() * 254 + 1);
                                }
                            });
                            return stats;
                        });
                    };
                    
                    return pc;
                };
                
                window.RTCPeerConnection.prototype = originalRTCPeerConnection.prototype;
            }
            
            // ===== 24. Crypto API timing protection =====
            
            if (window.crypto && window.crypto.subtle) {
                const originalGenerateKey = window.crypto.subtle.generateKey;
                const originalEncrypt = window.crypto.subtle.encrypt;
                const originalDecrypt = window.crypto.subtle.decrypt;
                
                window.crypto.subtle.generateKey = function(...args) {
                    return new Promise(resolve => {
                        const delay = Math.random() * 20 + 10;
                        setTimeout(() => {
                            resolve(originalGenerateKey.apply(this, args));
                        }, delay);
                    });
                };
                
                window.crypto.subtle.encrypt = function(...args) {
                    return new Promise(resolve => {
                        const delay = Math.random() * 10 + 5;
                        setTimeout(() => {
                            resolve(originalEncrypt.apply(this, args));
                        }, delay);
                    });
                };
                
                window.crypto.subtle.decrypt = function(...args) {
                    return new Promise(resolve => {
                        const delay = Math.random() * 10 + 5;
                        setTimeout(() => {
                            resolve(originalDecrypt.apply(this, args));
                        }, delay);
                    });
                };
            }
            
            // ===== 25. Human-like behavior simulation =====
            
            let mouseMovements = [];
            let keyboardEvents = [];
            let scrollEvents = [];
            let lastActivity = Date.now();
            
            document.addEventListener('mousemove', function(e) {
                const now = Date.now();
                mouseMovements.push({
                    x: e.clientX,
                    y: e.clientY,
                    timestamp: now,
                    deltaTime: now - lastActivity
                });
                
                if (mouseMovements.length > 50) {
                    mouseMovements = mouseMovements.slice(-25);
                }
                
                lastActivity = now;
            }, true);
            
            document.addEventListener('keydown', function(e) {
                const now = Date.now();
                keyboardEvents.push({
                    key: e.key,
                    code: e.code,
                    timestamp: now,
                    deltaTime: now - lastActivity
                });
                
                if (keyboardEvents.length > 20) {
                    keyboardEvents = keyboardEvents.slice(-10);
                }
                
                lastActivity = now;
            }, true);
            
            document.addEventListener('scroll', function(e) {
                const now = Date.now();
                scrollEvents.push({
                    scrollY: window.scrollY,
                    timestamp: now,
                    deltaTime: now - lastActivity
                });
                
                if (scrollEvents.length > 30) {
                    scrollEvents = scrollEvents.slice(-15);
                }
                
                lastActivity = now;
            }, true);
            
            setInterval(() => {
                const timeSinceLastActivity = Date.now() - lastActivity;
                
                if (timeSinceLastActivity > 30000 && Math.random() > 0.7) {
                    simulateSubtleActivity();
                }
            }, 10000);
            
            function simulateSubtleActivity() {
                if (Math.random() > 0.5) {
                    const event = new MouseEvent('mousemove', {
                        clientX: Math.random() * window.innerWidth,
                        clientY: Math.random() * window.innerHeight,
                        bubbles: true,
                        cancelable: true,
                        isTrusted: true
                    });
                    document.dispatchEvent(event);
                }
                
                if (Math.random() > 0.7) {
                    const scrollAmount = Math.random() * 100 - 50;
                    window.scrollBy({
                        top: scrollAmount,
                        behavior: 'smooth'
                    });
                }
                
                lastActivity = Date.now();
            }
            
            // ===== 26. Memory usage protection =====
            
            if (performance.memory) {
                const originalMemory = performance.memory;
                Object.defineProperty(performance, 'memory', {
                    get: () => ({
                        usedJSHeapSize: originalMemory.usedJSHeapSize + Math.floor(Math.random() * 1000000),
                        totalJSHeapSize: originalMemory.totalJSHeapSize + Math.floor(Math.random() * 1000000),
                        jsHeapSizeLimit: originalMemory.jsHeapSizeLimit + Math.floor(Math.random() * 1000000)
                    }),
                    configurable: true
                });
            }
            
            // ===== 27. Worker timing enhancement =====
            
            const originalWorker = window.Worker;
            if (originalWorker) {
                window.Worker = function(scriptURL, options) {
                    const worker = new originalWorker(scriptURL, options);
                    
                    const originalPostMessage = worker.postMessage;
                    worker.postMessage = function(message, transfer) {
                        setTimeout(() => {
                            originalPostMessage.call(this, message, transfer);
                        }, Math.random() * 5 + 1);
                    };
                    
                    return worker;
                };
                
                window.Worker.prototype = originalWorker.prototype;
            }
            
            // ===== 28. Notification API protection =====
            
            if (window.Notification) {
                const originalNotificationRequestPermission = Notification.requestPermission;
                Notification.requestPermission = function() {
                    return Promise.resolve('denied');
                };
                
                Object.defineProperty(Notification, 'permission', {
                    get: () => 'denied',
                    configurable: true
                });
            }
            
            // ===== 29. Console protection =====
            
            const originalLog = console.log;
            const originalWarn = console.warn;
            const originalError = console.error;
            
            console.log = function(...args) {
                if (!args.some(arg => typeof arg === 'string' && arg.includes('🔧'))) {
                    originalLog.apply(this, args);
                }
            };
            
            console.warn = function(...args) {
                if (!args.some(arg => typeof arg === 'string' && arg.includes('🔧'))) {
                    originalWarn.apply(this, args);
                }
            };
            
            console.error = function(...args) {
                if (!args.some(arg => typeof arg === 'string' && arg.includes('🔧'))) {
                    originalError.apply(this, args);
                }
            };
            
            // Cleanup temporary variables
            setTimeout(() => {
                try {
                    delete window.automationProperties;
                    delete window.createRealisticPlugins;
                    delete window.createRealisticMimeTypes;
                    delete window.createRealisticChromeRuntime;
                    delete window.createRealisticConnection;
                    delete window.simulateSubtleActivity;
                } catch (e) {}
            }, 1000);
            
            console.log('🔧 Browser Enhancement System v3.0 - Fully Activated');
            console.log('✅ All Fingerprint Protection Active');
            console.log('✅ Browser Signature Normalized');
            console.log('✅ Behavioral Patterns Established');
            console.log('✅ Ready for Automation Tasks');
            
        })();
        """

        # Inject all enhancement scripts
        await page.add_init_script(enhancement_part_1)
        await page.add_init_script(enhancement_part_2)
        await page.add_init_script(enhancement_part_3)
        await page.add_init_script(enhancement_part_4)

    @staticmethod
    async def add_human_behavior(page: Page):
        """Add natural human-like behavior patterns to the browser"""
        behavior_script = """
        (() => {
            'use strict';
            
            let isMoving = false;
            
            function simulateNaturalMouseMovement() {
                if (isMoving) return;
                isMoving = true;
                
                const startX = Math.random() * window.innerWidth;
                const startY = Math.random() * window.innerHeight;
                const endX = Math.random() * window.innerWidth;
                const endY = Math.random() * window.innerHeight;
                
                const steps = 20 + Math.floor(Math.random() * 30);
                let currentStep = 0;
                
                const moveInterval = setInterval(() => {
                    const progress = currentStep / steps;
                    const easeProgress = 1 - Math.pow(1 - progress, 3);
                    
                    const currentX = startX + (endX - startX) * easeProgress;
                    const currentY = startY + (endY - startY) * easeProgress;
                    
                    const event = new MouseEvent('mousemove', {
                        clientX: currentX + Math.random() * 2 - 1,
                        clientY: currentY + Math.random() * 2 - 1,
                        bubbles: true,
                        cancelable: true
                    });
                    
                    document.dispatchEvent(event);
                    
                    currentStep++;
                    if (currentStep >= steps) {
                        clearInterval(moveInterval);
                        isMoving = false;
                    }
                }, 16 + Math.random() * 8);
            }
            
            setInterval(() => {
                if (Math.random() < 0.3) {
                    simulateNaturalMouseMovement();
                }
            }, 5000 + Math.random() * 10000);
            
            let scrolling = false;
            function simulateNaturalScroll() {
                if (scrolling) return;
                scrolling = true;
                
                const scrollAmount = Math.random() * 200 + 50;
                const direction = Math.random() > 0.5 ? 1 : -1;
                let currentScroll = 0;
                
                const scrollInterval = setInterval(() => {
                    const step = (Math.random() * 10 + 5) * direction;
                    window.scrollBy(0, step);
                    currentScroll += Math.abs(step);
                    
                    if (currentScroll >= scrollAmount) {
                        clearInterval(scrollInterval);
                        scrolling = false;
                    }
                }, 16 + Math.random() * 8);
            }
            
            setInterval(() => {
                if (Math.random() < 0.2) {
                    simulateNaturalScroll();
                }
            }, 8000 + Math.random() * 12000);
            
            let focusState = true;
            setInterval(() => {
                if (Math.random() < 0.1) {
                    focusState = !focusState;
                    const event = new Event(focusState ? 'focus' : 'blur');
                    window.dispatchEvent(event);
                }
            }, 30000 + Math.random() * 60000);
            
            console.log('🎭 Human behavior simulation activated');
        })();
        """
        await page.add_init_script(behavior_script)

    @staticmethod
    def get_advanced_browser_args(user_agent, screen_config, proxy=None):
        """Get advanced browser arguments for realistic automation"""
        advanced_args = [
            f"--user-agent={user_agent}",
            f"--window-size={screen_config['width']},{screen_config['height']}",
            
            # Remove automation traces
            "--disable-blink-features=AutomationControlled",
            "--exclude-switches=enable-automation",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor",
            "--disable-extensions-except=",
            "--disable-extensions",
            
            # Network optimization
            "--aggressive-cache-discard",
            "--disable-background-networking",
            "--disable-background-timer-throttling",
            "--disable-renderer-backgrounding",
            "--disable-backgrounding-occluded-windows",
            "--disable-client-side-phishing-detection",
            
            # Graphics configuration
            "--use-gl=swiftshader",
            "--disable-gpu",
            "--disable-gpu-sandbox",
            "--disable-software-rasterizer",
            
            # Memory and performance optimization
            "--memory-pressure-off",
            "--max_old_space_size=4096",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            
            # Privacy settings
            "--disable-sync",
            "--disable-translate",
            "--disable-plugins-discovery",
            "--disable-preconnect",
            "--disable-link-doctor",
            
            # Fingerprint protection
            "--disable-canvas-aa",
            "--disable-2d-canvas-clip-aa",
            "--disable-gl-drawing-for-tests",
            
            # Audio settings
            "--mute-audio",
            "--disable-audio-output",
            
            # Detection prevention
            "--disable-ipc-flooding-protection",
            "--disable-hang-monitor",
            "--disable-prompt-on-repost",
            "--disable-domain-reliability",
            "--disable-component-extensions-with-background-pages",
            
            # Network enhancement
            "--enable-tcp-fast-open",
            "--enable-aggressive-domstorage-flushing",
            "--disable-background-mode",
            
            # Advanced settings
            "--no-first-run",
            "--no-service-autorun",
            "--password-store=basic",
            "--use-mock-keychain",
            "--disable-component-update",
            "--disable-default-apps",
            "--disable-dinosaur-easter-egg",
            
            # TLS configuration
            "--cipher-suite-blacklist=0x0001,0x0002,0x0004,0x0005,0x0017,0x0018,0xc002,0xc007,0xc00c,0xc011,0xc016",
            "--ssl-version-fallback-min=tls1.2",
            
            # Locale settings
            "--lang=en-US,ar-SA",
            
            # WebRTC protection
            "--force-webrtc-ip-handling-policy=disable_non_proxied_udp",
            "--disable-webrtc-multiple-routes",
            "--disable-webrtc-hw-decoding",
            "--disable-webrtc-hw-encoding"
        ]

        # Add proxy if provided
        if proxy:
            advanced_args.extend([
                f"--proxy-server={proxy}",
                "--proxy-bypass-list=<-loopback>"
            ])
            
        return advanced_args

    @staticmethod
    def get_advanced_headers():
        """Get advanced headers for realistic HTTP requests"""
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,ar-SA;q=0.8,ar;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'DNT': '1',
            'Connection': 'keep-alive'
        }