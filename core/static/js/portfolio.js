const codeLines = [
    {text: '# Um Desenvolvedor Backend em ação', type: 'comment'},
    {text: 'class Developer:', type: 'keyword'},
    {text: '    def __init__(self, name, stack):', type: 'keyword'},
    {text: '        self.name = name', type: 'variable'},
    {text: '        self.stack = stack', type: 'variable'},
    {text: '', type: 'empty'},
    {text: '    def code(self):', type: 'keyword'},
    {text: '        print(f"{self.name} está codando em {self.stack[0]}...")', type: 'function'},
    {text: '', type: 'empty'},
    {text: '# Criando uma instância', type: 'comment'},
    {text: 'me = Developer(', type: 'variable'},
    {text: '    name="Jhonatan Rian",', type: 'variable'},
    {text: '    stack=["Python", "Django", "Docker"]', type: 'variable'},
    {text: ')', type: 'variable'},
    {text: '', type: 'empty'},
    {text: 'me.code()', type: 'function'},
];

const codeEditor = document.getElementById('code-editor');
const typingSpeed = 80;
const deletingSpeed = 30;
const delayBetweenLines = 500;
const delayAfterTyping = 3000;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getStyledLine(line) {
    switch (line.type) {
        case 'comment':
            return `<span class="token-comment">${line.text}</span>`;
        case 'keyword':
            return line.text.replace(/(class|def|self)/g, '<span class="token-keyword">$1</span>');
        case 'function':
            return line.text.replace(/(\w+)\(.*\)/, '<span class="token-function">$1</span>()').replace(/f"(.+?)"/, `<span class="token-string">f"$1"</span>`);
        case 'variable':
            return line.text.replace(/"(.*?)"/g, '<span class="token-string">"$1"</span>');
        default:
            return line.text;
    }
}

async function typeWriter() {
    if (!codeEditor) return;

    while (true) {
        codeEditor.innerHTML = ''; // Limpa o editor
        for (let i = 0; i < codeLines.length; i++) {
            const line = codeLines[i];
            if (line.type === 'empty') {
                codeEditor.innerHTML += '<br>';
                await sleep(delayBetweenLines);
                continue;
            }

            const styledLine = getStyledLine(line);
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = styledLine;

            const nodes = Array.from(tempDiv.childNodes);
            let currentLineHTML = '';

            for (const node of nodes) {
                if (node.nodeType === Node.TEXT_NODE) {
                    for (const char of node.textContent) {
                        currentLineHTML += char;
                        codeEditor.innerHTML = codeEditor.innerHTML.split('<br>').slice(0, -1).join('<br>') + (i > 0 ? '<br>' : '') + currentLineHTML;
                        await sleep(typingSpeed);
                    }
                } else {
                    const outerHTML = node.outerHTML;
                    let tempNodeHTML = '';
                    for (const char of outerHTML) {
                        tempNodeHTML += char;
                        codeEditor.innerHTML = codeEditor.innerHTML.split('<br>').slice(0, -1).join('<br>') + (i > 0 ? '<br>' : '') + currentLineHTML + tempNodeHTML;
                        await sleep(typingSpeed / 2);
                    }
                    currentLineHTML += outerHTML;
                }
            }
            codeEditor.innerHTML += '<br>';
        }

        await sleep(delayAfterTyping);

        // Deleting effect
        let lines = codeEditor.innerHTML.split('<br>');
        for (let i = lines.length - 1; i >= 0; i--) {
            let line = lines[i];
            while (line.length > 0) {
                line = line.slice(0, -1);
                lines[i] = line;
                codeEditor.innerHTML = lines.join('<br>');
                await sleep(deletingSpeed);
            }
            lines.pop();
        }
    }
}

document.addEventListener('DOMContentLoaded', typeWriter);