class BrowserHistory {
    private backStack: string[] = [];
    private forwardStack: string[] = [];
    private current: string;
    
    constructor(paginaInicial: string) {
        this.current = paginaInicial;
    }

    visit(url: string): void {
        this.backStack.push(this.current);
        this.current = url;
        this.forwardStack = [];  
    }

    back(): string | null {
        if (this.backStack.length === 0) {
            return null;
        }

        const prev = this.backStack.pop()!;
        this.forwardStack.push(this.current);
        this.current = prev;
        return this.current;
        
    }

    getCurrentPage(): string {
        return this.current;
    }

}

const navegador = new BrowserHistory("home.com");
console.log(navegador.getCurrentPage()); // "home.com"
navegador.visit("google.com");
navegador.visit("openai.com");
console.log(navegador.getCurrentPage()); // "openai.com"
navegador.back(); // retorna "google.com"