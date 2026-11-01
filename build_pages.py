import os
import html

SECTIONS = [
    {
        "id": "q1",
        "tag": "Q1: Lab Network Topology, Interfaces, Routers & IP Pools",
        "badge": "Theory / Study",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "1. To familiarize with the Lab Network Topology, Locating different interfaces, routers and switches. Studying different pools of IP addresses.",
        "files": [
            {"name": "Q1_Lab_Network_Topology.txt", "type": "txt", "title": "Network Topology & IP Pools Report"}
        ]
    },
    {
        "id": "q2",
        "tag": "Q2: Networking Commands (PING, TRACEROUTE), Telnet & Delay",
        "badge": "Theory / Experimental",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "2. To learn and observe the usage of different networking commands e.g. PING, TRACEROUTE. Learning remote login using telnet session. Measuring typical average delays between different locations of the network.",
        "files": [
            {"name": "Q2_Networking_Commands_and_Delays.txt", "type": "txt", "title": "Networking Commands & Delay Analysis"}
        ]
    },
    {
        "id": "q3",
        "tag": "Q3: Ping Tool Statistics & Round-Trip Times",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "3. \"Ping\" is a tool used to determine if a server is responding and to estimate the round trip time of a message sent to that server. Use the ping command for the following URLs and record the success or failure statistics along with the average round trip time:\n a) google.com   b) facebook.com   c) bitmesra.ac.in",
        "files": [
            {"name": "Q3_Ping_Statistics.txt", "type": "txt", "title": "All Ping Statistics"},
            {"name": "Q3_1_Ping_Google.txt", "type": "txt", "title": "3.1 google.com"},
            {"name": "Q3_2_Ping_Facebook.txt", "type": "txt", "title": "3.2 facebook.com"},
            {"name": "Q3_3_Ping_BitMesra.txt", "type": "txt", "title": "3.3 bitmesra.ac.in"}
        ]
    },
    {
        "id": "q4",
        "tag": "Q4: Trace Route Path Analysis",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "4. Trace the route that is taken when you try to access:\n a) google.com   b) facebook.com   c) bitmesra.ac.in",
        "files": [
            {"name": "Q4_Trace_Route.txt", "type": "txt", "title": "All Route Traces"},
            {"name": "Q4_1_Trace_Google.txt", "type": "txt", "title": "4.1 google.com"},
            {"name": "Q4_2_Trace_Facebook.txt", "type": "txt", "title": "4.2 facebook.com"},
            {"name": "Q4_3_Trace_BitMesra.txt", "type": "txt", "title": "4.3 bitmesra.ac.in"}
        ]
    },
    {
        "id": "q5",
        "tag": "Q5: IPv4 Class Determination",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "question": "5. Write a C/C++ program to determine if the IP address is in Class A, B, C, D, or E.",
        "files": [
            {"name": "Q5_IP_Class_Determination.c", "type": "c", "title": "IPv4 Class Identifier"}
        ]
    },
    {
        "id": "q6",
        "tag": "Q6: Dotted Decimal to 32-bit Address Translation",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "question": "6. Write a C/C++ program to translate dotted decimal IP address into 32 bit address.",
        "files": [
            {"name": "Q6_Dotted_Decimal_To_32Bit.c", "type": "c", "title": "Dotted Decimal to 32-Bit Binary & Hex"}
        ]
    },
    {
        "id": "q7",
        "tag": "Q7: Bit Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "question": "7. Write a C/C++ program to perform bit stuffing and de-stuffing.",
        "files": [
            {"name": "Q7_Bit_Stuffing_Destuffing.c", "type": "c", "title": "HDLC Bit Stuffing & Framing"}
        ]
    },
    {
        "id": "q8",
        "tag": "Q8: Character Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "question": "8. Write a C/C++ program to perform character stuffing and de-stuffing.",
        "files": [
            {"name": "Q8_Character_Stuffing_Destuffing.c", "type": "c", "title": "Byte Stuffing (DLE STX / DLE ETX)"}
        ]
    },
    {
        "id": "q9",
        "tag": "Q9: Error Detection Methods",
        "badge": "C Code (4 Methods)",
        "unit": "Unit 4: Error Detection & Correction",
        "question": "9. Write a C/C++ program to perform error detection method using:\n - Single parity checking method\n - Two dimension parity checking method\n - Cyclic redundancy check (CRC) method\n - Internet checksum method",
        "files": [
            {"name": "Q9_1_Single_Parity.c", "type": "c", "title": "9.1 Single Parity"},
            {"name": "Q9_2_Two_Dimension_Parity.c", "type": "c", "title": "9.2 2D Parity (LRC)"},
            {"name": "Q9_3_CRC.c", "type": "c", "title": "9.3 CRC (Modulo-2 XOR)"},
            {"name": "Q9_4_Internet_Checksum.c", "type": "c", "title": "9.4 Internet Checksum"}
        ]
    },
    {
        "id": "q10",
        "tag": "Q10: Error Correction using Hamming Code",
        "badge": "C Code",
        "unit": "Unit 4: Error Detection & Correction",
        "question": "10. Write a C/C++ program to perform error correction using Hamming code method.",
        "files": [
            {"name": "Q10_Hamming_Code.c", "type": "c", "title": "Hamming (7, 4) Code Encoding & Correction"}
        ]
    },
    {
        "id": "q11",
        "tag": "Q11: Socket Programming & Client-Server Model",
        "badge": "Study & C Code",
        "unit": "Unit 5: Socket Programming & HTTP",
        "question": "11. Study and implement model for Socket Programming and Client - Server model.",
        "files": [
            {"name": "Q11_1_Socket_Server.c", "type": "c", "title": "11.1 TCP Server"},
            {"name": "Q11_2_Socket_Client.c", "type": "c", "title": "11.2 TCP Client"},
            {"name": "Q11_Socket_Programming_Model.txt", "type": "txt", "title": "Socket Theory & Architecture"}
        ]
    },
    {
        "id": "q12",
        "tag": "Q12: HTTP Sockets: Web Page Upload & Download",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 5: Socket Programming & HTTP",
        "question": "12. Create a socket for HTTP for web page upload and download.",
        "files": [
            {"name": "Q12_1_HTTP_Download.c", "type": "c", "title": "12.1 HTTP GET Download"},
            {"name": "Q12_2_HTTP_Upload.c", "type": "c", "title": "12.2 HTTP POST Upload"}
        ]
    },
    {
        "id": "q13",
        "tag": "Q13: Simulation of PING & TRACEROUTE Commands",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 6: Protocol Simulations",
        "question": "13. Write a code simulating PING and TRACEROUTE commands.",
        "files": [
            {"name": "Q13_1_Ping_Simulation.c", "type": "c", "title": "13.1 PING Simulator"},
            {"name": "Q13_2_Traceroute_Simulation.c", "type": "c", "title": "13.2 TRACEROUTE Simulator"}
        ]
    },
    {
        "id": "q14",
        "tag": "Q14: DHCP Server Simulation (DORA)",
        "badge": "C Code",
        "unit": "Unit 6: Protocol Simulations",
        "question": "14. Write a code simulating DHCP server.",
        "files": [
            {"name": "Q14_DHCP_Server_Simulation.c", "type": "c", "title": "DHCP Server Simulator (DORA)"}
        ]
    },
    {
        "id": "q15",
        "tag": "Q15: Routing Table Implementation",
        "badge": "C Code (2 Algorithms)",
        "unit": "Unit 7: Routing Algorithms",
        "question": "15. Implement the routing table using:\n a) Dijkstra's algorithm.\n b) Distance vector Routing algorithm.",
        "files": [
            {"name": "Q15_1_Dijkstra_Routing.c", "type": "c", "title": "15.1 Dijkstra (OSPF)"},
            {"name": "Q15_2_Distance_Vector_Routing.c", "type": "c", "title": "15.2 Distance Vector (RIP)"}
        ]
    }
]

def read_file_content(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def generate_html():
    current_unit = ""
    sidebar_items_html = ""
    sections_html = ""

    for s in SECTIONS:
        if s["unit"] != current_unit:
            current_unit = s["unit"]
            sidebar_items_html += f'<div class="unit-header">{html.escape(current_unit)}</div>\n'
        
        badge_type = s["files"][0]["type"].upper()

        sidebar_items_html += f'''
        <a href="#{s["id"]}" class="nav-item" onclick="highlightNav(this)">
            <span class="nav-tag nav-tag-{s["files"][0]["type"]}">{badge_type}</span>
            <span class="nav-title">{html.escape(s["tag"])}</span>
        </a>
        '''

        files_tabs_html = ""
        files_content_html = ""

        for idx, f in enumerate(s["files"]):
            fname = f["name"]
            ftitle = f["title"]
            ftype = f["type"]
            fcontent = read_file_content(fname)
            escaped_code = html.escape(fcontent)
            is_active = "active" if idx == 0 else ""
            content_id = f"{s['id']}_content_{idx}"
            lang_class = "language-c" if ftype == "c" else "language-none"

            files_tabs_html += f'''
            <button class="tab-btn {is_active}" onclick="switchTab('{s["id"]}', {idx})">
                {html.escape(ftitle)}
            </button>
            '''

            files_content_html += f'''
            <div id="{content_id}" class="tab-content {is_active}">
                <div class="code-header">
                    <span class="file-name">📄 <a href="{fname}" target="_blank">{html.escape(fname)}</a></span>
                    <div class="code-actions">
                        <button class="action-btn copy-btn" onclick="copySnippet('{content_id}_code', this)">
                            📋 Copy Code
                        </button>
                        <a href="{fname}" download class="action-btn download-btn">⬇ Download</a>
                    </div>
                </div>
                <pre class="code-block"><code id="{content_id}_code" class="{lang_class}">{escaped_code}</code></pre>
            </div>
            '''

        escaped_q = html.escape(s["question"]).replace("\n", "<br>")

        sections_html += f'''
        <section id="{s["id"]}" class="question-card">
            <div class="card-header">
                <div class="card-title-group">
                    <span class="badge badge-{s["files"][0]["type"]}">{html.escape(s["badge"])}</span>
                    <h2 class="card-title">{html.escape(s["tag"])}</h2>
                </div>
                <div class="header-actions">
                    <button class="main-copy-btn" onclick="copyActiveSolution('{s["id"]}', this)">
                        <span class="copy-icon">📋</span> Copy Solution
                    </button>
                    <a href="#{s["id"]}" class="anchor-link" title="Direct link to this question">🔗</a>
                </div>
            </div>
            
            <div class="problem-box">
                <span class="problem-label">Assignment Question:</span>
                <p>{escaped_q}</p>
            </div>

            <div class="tabs-container">
                <div class="tab-buttons-bar">
                    {files_tabs_html}
                </div>
                {files_content_html}
            </div>
        </section>
        '''

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT302 DCCN Lab Assignment Solutions & Source Code</title>
    <meta name="description" content="Clean C programs and empirical reports for IT302 Data Communication and Computer Networks Lab Assignment.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        :root {{
            --bg-color: #090d16;
            --surface-color: #131b2e;
            --surface-card: #182238;
            --surface-hover: #22304e;
            --border-color: #273656;
            --border-accent: #3b82f6;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent-blue: #38bdf8;
            --accent-green: #22c55e;
            --accent-purple: #c084fc;
            --accent-amber: #f59e0b;
            --code-bg: #070b12;
            --sidebar-width: 290px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        html {{
            scroll-behavior: smooth;
            width: 100%;
            overflow-x: hidden;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            display: grid;
            grid-template-columns: var(--sidebar-width) minmax(0, 1fr);
            min-height: 100vh;
            width: 100%;
            max-width: 100vw;
            overflow-x: hidden;
        }}

        /* Custom Modern Scrollbars - Sleek & Dark */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: #090d16;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #273656;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #38bdf8;
        }}
        * {{
            scrollbar-width: thin;
            scrollbar-color: #273656 #090d16;
        }}

        /* Sidebar Styling */
        #sidebar {{
            background-color: var(--surface-color);
            border-right: 1px solid var(--border-color);
            height: 100vh;
            position: sticky;
            top: 0;
            overflow-y: auto;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            z-index: 50;
        }}

        .sidebar-header {{
            padding: 20px 16px 14px;
            border-bottom: 1px solid var(--border-color);
            background: #0d1424;
        }}

        .sidebar-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--accent-blue);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .sidebar-subtitle {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 2px;
        }}

        .search-box {{
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-color);
            background: #0d1424;
        }}

        .search-input {{
            width: 100%;
            padding: 8px 12px;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-primary);
            font-size: 0.8rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-input:focus {{
            border-color: var(--accent-blue);
        }}

        .nav-list {{
            flex: 1;
            padding: 8px 0 24px;
        }}

        .unit-header {{
            padding: 14px 14px 4px;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 700;
            color: var(--accent-amber);
        }}

        .nav-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 7px 14px;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.8rem;
            transition: all 0.15s ease;
            border-left: 3px solid transparent;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .nav-item:hover, .nav-item.active {{
            background-color: var(--surface-hover);
            color: var(--text-primary);
            border-left-color: var(--accent-blue);
        }}

        .nav-tag {{
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            font-size: 0.65rem;
            padding: 2px 5px;
            border-radius: 4px;
            flex-shrink: 0;
        }}

        .nav-tag-c {{
            background: rgba(34, 197, 94, 0.15);
            color: var(--accent-green);
            border: 1px solid rgba(34, 197, 94, 0.3);
        }}

        .nav-tag-txt {{
            background: rgba(192, 132, 252, 0.15);
            color: var(--accent-purple);
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .nav-title {{
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        /* Main Content Layout */
        #main {{
            min-width: 0;
            width: 100%;
            padding: 28px 36px 64px;
            overflow-x: hidden;
        }}

        .hero-banner {{
            background: linear-gradient(135deg, #131b2e 0%, #0d1424 100%);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 28px 32px;
            margin-bottom: 32px;
            position: relative;
        }}

        .hero-title {{
            font-size: 1.7rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }}

        .hero-desc {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-bottom: 20px;
            max-width: 900px;
        }}

        .hero-buttons {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
            cursor: pointer;
            border: 1px solid transparent;
        }}

        .btn-primary {{
            background-color: var(--accent-blue);
            color: #090d16;
        }}

        .btn-primary:hover {{
            background-color: #7dd3fc;
            box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
        }}

        .btn-secondary {{
            background-color: var(--surface-card);
            border-color: var(--border-color);
            color: var(--text-primary);
        }}

        .btn-secondary:hover {{
            background-color: var(--surface-hover);
        }}

        /* Question Cards */
        .question-card {{
            background-color: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 32px;
            scroll-margin-top: 24px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            min-width: 0;
            max-width: 100%;
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            padding-bottom: 14px;
            flex-wrap: wrap;
        }}

        .card-title-group {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            min-width: 0;
            flex: 1;
        }}

        .card-title {{
            font-size: 1.2rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.01em;
            word-break: break-word;
        }}

        .badge {{
            font-size: 0.7rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            flex-shrink: 0;
        }}

        .badge-c {{
            background: rgba(34, 197, 94, 0.15);
            color: var(--accent-green);
            border: 1px solid rgba(34, 197, 94, 0.3);
        }}

        .badge-txt {{
            background: rgba(192, 132, 252, 0.15);
            color: var(--accent-purple);
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        /* Prominent Main Copy Button */
        .main-copy-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: #ffffff;
            border: 1px solid #3b82f6;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
        }}

        .main-copy-btn:hover {{
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
        }}

        .main-copy-btn.copied {{
            background: linear-gradient(135deg, #16a34a, #15803d) !important;
            border-color: #22c55e !important;
            box-shadow: 0 2px 10px rgba(34, 197, 94, 0.4) !important;
        }}

        .anchor-link {{
            color: var(--text-muted);
            text-decoration: none;
            font-size: 1.1rem;
            transition: color 0.2s;
        }}

        .anchor-link:hover {{
            color: var(--accent-blue);
        }}

        .problem-box {{
            background-color: rgba(9, 13, 22, 0.7);
            border-left: 4px solid var(--accent-blue);
            padding: 12px 16px;
            border-radius: 4px;
            margin-bottom: 18px;
            font-size: 0.9rem;
            color: #cbd5e1;
            word-break: break-word;
        }}

        .problem-label {{
            color: var(--accent-blue);
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 700;
            display: block;
            margin-bottom: 4px;
        }}

        /* Tabs Styling */
        .tabs-container {{
            margin-top: 14px;
            min-width: 0;
            max-width: 100%;
        }}

        .tab-buttons-bar {{
            display: flex;
            gap: 4px;
            overflow-x: auto;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 12px;
            padding-bottom: 2px;
            scrollbar-width: none;
        }}
        .tab-buttons-bar::-webkit-scrollbar {{
            display: none;
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 7px 14px;
            font-size: 0.82rem;
            font-weight: 500;
            cursor: pointer;
            border-radius: 6px 6px 0 0;
            border-bottom: 2px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}

        .tab-btn:hover {{
            color: var(--text-primary);
            background-color: rgba(255,255,255,0.03);
        }}

        .tab-btn.active {{
            color: var(--accent-blue);
            border-bottom-color: var(--accent-blue);
            font-weight: 600;
            background-color: rgba(56, 189, 248, 0.08);
        }}

        .tab-content {{
            display: none;
            min-width: 0;
            max-width: 100%;
        }}

        .tab-content.active {{
            display: block;
        }}

        .code-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #0b111e;
            padding: 8px 14px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border: 1px solid var(--border-color);
            border-bottom: none;
            font-size: 0.78rem;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .file-name a {{
            color: var(--accent-blue);
            text-decoration: none;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 500;
        }}

        .file-name a:hover {{
            text-decoration: underline;
        }}

        .code-actions {{
            display: flex;
            gap: 6px;
        }}

        .action-btn {{
            background-color: var(--surface-hover);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.15s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .action-btn:hover {{
            background-color: var(--border-accent);
            color: #ffffff;
        }}

        .code-block {{
            background-color: var(--code-bg) !important;
            border: 1px solid var(--border-color);
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            padding: 16px !important;
            margin: 0 !important;
            max-height: 480px;
            overflow-x: auto !important;
            overflow-y: auto !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.82rem !important;
            line-height: 1.55 !important;
            white-space: pre !important;
            word-wrap: normal !important;
            max-width: 100% !important;
        }}

        /* Toast notification */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: linear-gradient(135deg, #15803d, #16a34a);
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.88rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.5);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        #toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        /* Mobile Responsive */
        @media (max-width: 900px) {{
            body {{
                grid-template-columns: 1fr;
            }}
            #sidebar {{
                display: none;
            }}
            #main {{
                padding: 16px;
            }}
            .hero-banner {{
                padding: 20px;
            }}
            .card-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
            .header-actions {{
                width: 100%;
                justify-content: space-between;
            }}
        }}
    </style>
</head>
<body>

    <!-- Left Sticky Sidebar -->
    <nav id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-title">⚡ IT302 DCCN LAB</div>
            <div class="sidebar-subtitle">Assignments & Source Codes</div>
        </div>
        <div class="search-box">
            <input type="text" id="search-input" class="search-input" placeholder="Search questions..." onkeyup="filterQuestions()">
        </div>
        <div class="nav-list" id="nav-list">
            {sidebar_items_html}
        </div>
    </nav>

    <!-- Main Content Area -->
    <main id="main">
        <header class="hero-banner">
            <h1 class="hero-title">IT302 — Data Communication & Computer Networks</h1>
            <p class="hero-desc">
                Laboratory assignment solutions portal with short, crisp C source code implementations, 
                empirical networking statistics (PING, Traceroute), and study reports.
            </p>
            <div class="hero-buttons">
                <a href="https://github.com/Aryan9891/DCCN-Lab-repo" target="_blank" class="btn btn-primary">
                    ⭐ GitHub Repository
                </a>
                <a href="IT302 DCCNLAB ASSIGNMENT.pdf" target="_blank" class="btn btn-secondary">
                    📄 Assignment PDF
                </a>
                <a href="README.md" target="_blank" class="btn btn-secondary">
                    📋 README Guide
                </a>
            </div>
        </header>

        <div id="questions-container">
            {sections_html}
        </div>
    </main>

    <div id="toast">
        <span>✓</span> <span id="toast-text">Copied to clipboard!</span>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script>
        function switchTab(sectionId, tabIndex) {{
            const card = document.getElementById(sectionId);
            if (!card) return;
            const buttons = card.querySelectorAll('.tab-btn');
            const contents = card.querySelectorAll('.tab-content');

            buttons.forEach((btn, idx) => {{
                btn.classList.toggle('active', idx === tabIndex);
            }});

            contents.forEach((cnt, idx) => {{
                cnt.classList.toggle('active', idx === tabIndex);
            }});
        }}

        // Copy currently active tab solution
        function copyActiveSolution(sectionId, buttonEl) {{
            const card = document.getElementById(sectionId);
            if (!card) return;
            const activeContent = card.querySelector('.tab-content.active code') || card.querySelector('code');
            if (!activeContent) return;

            copyText(activeContent.innerText, buttonEl, "✓ Solution Copied!");
        }}

        // Copy individual snippet from tab code header
        function copySnippet(elementId, buttonEl) {{
            const codeEl = document.getElementById(elementId);
            if (!codeEl) return;
            copyText(codeEl.innerText, buttonEl, "✓ Code Copied!");
        }}

        function copyText(text, buttonEl, successMsg) {{
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(text).then(() => {{
                    triggerSuccessUI(buttonEl, successMsg);
                }}).catch(() => {{
                    fallbackCopy(text, buttonEl, successMsg);
                }});
            }} else {{
                fallbackCopy(text, buttonEl, successMsg);
            }}
        }}

        function fallbackCopy(text, buttonEl, successMsg) {{
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.left = '-9999px';
            document.body.appendChild(ta);
            ta.select();
            try {{
                document.execCommand('copy');
                triggerSuccessUI(buttonEl, successMsg);
            }} catch (e) {{
                showToast("Failed to copy!");
            }}
            document.body.removeChild(ta);
        }}

        function triggerSuccessUI(buttonEl, message) {{
            showToast(message);
            if (buttonEl) {{
                const originalText = buttonEl.innerHTML;
                buttonEl.innerHTML = "✓ Copied!";
                buttonEl.classList.add('copied');
                setTimeout(() => {{
                    buttonEl.innerHTML = originalText;
                    buttonEl.classList.remove('copied');
                }}, 2000);
            }}
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            const toastText = document.getElementById('toast-text');
            if (toastText) toastText.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2200);
        }}

        function filterQuestions() {{
            const query = document.getElementById('search-input').value.toLowerCase();
            const navItems = document.querySelectorAll('.nav-item');
            const cards = document.querySelectorAll('.question-card');

            navItems.forEach(item => {{
                const text = item.innerText.toLowerCase();
                item.style.display = text.includes(query) ? 'flex' : 'none';
            }});

            cards.forEach(card => {{
                const text = card.innerText.toLowerCase();
                card.style.display = text.includes(query) ? 'block' : 'none';
            }});
        }}

        function highlightNav(el) {{
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            el.classList.add('active');
        }}
    </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("index.html regenerated with clean responsive CSS and prominent copy buttons!")

if __name__ == "__main__":
    generate_html()
