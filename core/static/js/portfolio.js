const codeLines = [
    { text: "def solve_problems():", type: "function_def" },
    { text: "    while awake:", type: "keyword_block" },
    { text: "        write_code()", type: "call" },
    { text: "        run_tests()", type: "call" },
    { text: "        deploy()", type: "call" },
    { text: "    return \"Success!\"", type: "return_stmt" }
];

const codeEditor = document.getElementById('code-editor');

function getHighlightedChar(char, type, lineText, charIndex) {
    if (type === 'function_def') {
        if (charIndex < 3) return `<span class="token-keyword">${char}</span>`;
        if (charIndex > 3 && charIndex < lineText.indexOf('(')) return `<span class="token-function">${char}</span>`;
    }
    if (type === 'keyword_block') {
        if (charIndex >= 4 && charIndex < 9) return `<span class="token-keyword">${char}</span>`;
        if (charIndex >= 10 && charIndex < 15) return `<span class="token-variable">${char}</span>`;
    }
    if (type === 'call') {
         if (charIndex >= 8 && charIndex < lineText.indexOf('(')) return `<span class="token-function">${char}</span>`;
    }
    if (type === 'return_stmt') {
        if (charIndex >= 4 && charIndex < 10) return `<span class="token-keyword">${char}</span>`;
        if (charIndex >= 11) return `<span class="token-string">${char}</span>`;
    }
    return char;
}

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function typeWriter() {
    if (!codeEditor) return;

    while (true) {
        codeEditor.innerHTML = '<span class="blinking-cursor"></span>';
        
        let fullHtml = '';
        for (let i = 0; i < codeLines.length; i++) {
            const line = codeLines[i];
            let lineHtml = '';
            
            for (let j = 0; j < line.text.length; j++) {
                const char = line.text[j];
                lineHtml += getHighlightedChar(char, line.type, line.text, j);
                
                codeEditor.innerHTML = fullHtml + lineHtml + '<span class="blinking-cursor"></span>';
                
                let delay = Math.random() * (100 - 30) + 30;
                if (char === ':' && (line.type === 'function_def' || line.type === 'keyword_block')) {
                    delay += 500;
                }
                await sleep(delay);
            }
            fullHtml += lineHtml + '\n';
            codeEditor.innerHTML = fullHtml + '<span class="blinking-cursor"></span>';
            await sleep(500);
        }

        await sleep(2000);

        // Backspace effect
        let plainText = "";
        codeLines.forEach(l => plainText += l.text + '\n');
        let totalChars = plainText.length;

        for(let i = 0; i < totalChars; i++) {
            let charsToKeep = totalChars - i - 1;
            
            let newHtml = '';
            let kept = 0;
            for(let k=0; k<codeLines.length; k++) {
                let lineStr = "";
                for(let j=0; j<codeLines[k].text.length; j++) {
                    if(kept < charsToKeep) {
                        lineStr += getHighlightedChar(codeLines[k].text[j], codeLines[k].type, codeLines[k].text, j);
                        kept++;
                    }
                }
                if(lineStr.length > 0) newHtml += lineStr;
                if(kept < charsToKeep && k < codeLines.length - 1) {
                    newHtml += '\n';
                    kept++;
                }
            }
            
            codeEditor.innerHTML = newHtml + '<span class="blinking-cursor"></span>';
            await sleep(20);
        }
        await sleep(500);
    }
}


document.addEventListener('DOMContentLoaded', () => {
    // Start type writer effect
    typeWriter();

    // Mobile menu toggle logic
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');

    if (mobileMenuButton && mobileMenu && menuIcon) {
        mobileMenuButton.addEventListener('click', () => {
            const isHidden = mobileMenu.classList.contains('hidden');
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                menuIcon.textContent = 'close';
            } else {
                mobileMenu.classList.add('hidden');
                menuIcon.textContent = 'menu';
            }
        });

        // Close mobile menu when clicking any link inside it
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                menuIcon.textContent = 'menu';
            });
        });

        // Close mobile menu if window is resized to desktop width
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768) {
                mobileMenu.classList.add('hidden');
                menuIcon.textContent = 'menu';
            }
        });
    }
});