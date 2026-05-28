class SidebarManager {
    constructor() {
        this.sidebar = document.getElementById('sidebar');
        this.mainContent = document.getElementById('main-content');
        this.sidebarToggle = document.getElementById('sidebar-toggle');
        this.toggleIconOpen = document.getElementById('toggle-icon-open');
        this.toggleIconClose = document.getElementById('toggle-icon-close');
        
        this.COLLAPSED_WIDTH_CLASS = 'w-20';
        this.EXPANDED_WIDTH_CLASS = 'w-72';
        this.COLLAPSED_MARGIN = '80px';
        this.EXPANDED_MARGIN = '288px';
        this.COLLAPSED_BUTTON_LEFT = '60px';
        this.EXPANDED_BUTTON_LEFT = '268px';
        
        this.init();
    }

    init() {
        if (!this.sidebar || !this.mainContent || !this.sidebarToggle) return;
        
        this.sidebarToggle.addEventListener('click', () => {
            const isCurrentlyExpanded = this.sidebar.classList.contains(this.EXPANDED_WIDTH_CLASS);
            const willCollapse = isCurrentlyExpanded;
            this.setSidebarState(willCollapse);
            localStorage.setItem('sidebar-collapsed', willCollapse);
        });

        document.querySelectorAll('[data-submenu-trigger]').forEach(trigger => {
            trigger.addEventListener('click', (e) => this.handleSubmenuToggle(e, trigger));
        });

        const savedState = localStorage.getItem('sidebar-collapsed') === 'true';
        this.setSidebarState(savedState);

        // Auto-expand submenus if they contain an active link and sidebar is not collapsed
        if (!savedState) {
            document.querySelectorAll('[data-submenu-list]').forEach(submenu => {
                const hasActiveLink = submenu.querySelector('.bg-yellow-300') !== null;
                if (hasActiveLink) {
                    submenu.classList.add('open');
                    const trigger = submenu.previousElementSibling;
                    const icon = trigger.querySelector('[data-submenu-icon]');
                    if (icon) icon.classList.add('rotate-180');
                }
            });
        }
    }

    setSidebarState(isCollapsed) {
        this.sidebar.classList.toggle('sidebar-collapsed', isCollapsed);
        this.sidebar.classList.toggle(this.EXPANDED_WIDTH_CLASS, !isCollapsed);
        this.sidebar.classList.toggle(this.COLLAPSED_WIDTH_CLASS, isCollapsed);

        this.mainContent.style.marginLeft = isCollapsed ? this.COLLAPSED_MARGIN : this.EXPANDED_MARGIN;
        this.sidebarToggle.style.left = isCollapsed ? this.COLLAPSED_BUTTON_LEFT : this.EXPANDED_BUTTON_LEFT;

        if (this.toggleIconOpen) this.toggleIconOpen.classList.toggle('hidden', !isCollapsed);
        if (this.toggleIconClose) this.toggleIconClose.classList.toggle('hidden', isCollapsed);

        if (isCollapsed) {
            document.querySelectorAll('[data-submenu-list]').forEach(submenu => {
                submenu.classList.remove('open');
                const icon = submenu.previousElementSibling.querySelector('[data-submenu-icon]');
                if (icon) icon.classList.remove('rotate-180');
            });
        }
    }

    handleSubmenuToggle(e, trigger) {
        if (this.sidebar.classList.contains('sidebar-collapsed')) {
            this.setSidebarState(false);
            localStorage.setItem('sidebar-collapsed', false);
        }

        const submenuList = trigger.nextElementSibling;
        const submenuIcon = trigger.querySelector('[data-submenu-icon]');

        if (submenuList) submenuList.classList.toggle('open');
        if (submenuIcon) submenuIcon.classList.toggle('rotate-180');
    }
}

class DropdownManager {
    constructor() {
        this.init();
    }

    init() {
        document.addEventListener('click', this.handleDocumentClick.bind(this));
    }

    handleDocumentClick(event) {
        const isDropdownButton = event.target.closest('[data-dropdown-button]');
        
        if (!isDropdownButton && !event.target.closest('[data-dropdown-container]')) {
            this.closeAllDropdowns();
            return;
        }

        if (isDropdownButton) {
            const container = isDropdownButton.closest('[data-dropdown-container]');
            if (!container) return;
            const menu = container.querySelector('[data-dropdown-menu]');
            
            if (menu) {
                const isHidden = menu.classList.contains('hidden');
                this.closeAllDropdowns();
                if (isHidden) {
                    menu.classList.remove('hidden');
                }
            }
        }
    }

    closeAllDropdowns() {
        document.querySelectorAll('[data-dropdown-menu]').forEach(menu => {
            menu.classList.add('hidden');
        });
    }
}

class TabsManager {
    constructor() {
        this.init();
    }

    init() {
        document.querySelectorAll('[data-tabs-container]').forEach(tabsContainer => {
            const tabList = tabsContainer.querySelector('[data-tab-list]');
            if (!tabList) return;
            const tabTriggers = tabList.querySelectorAll('[data-tab-trigger]');
            const tabContents = tabsContainer.querySelectorAll('[data-tab-content]');

            tabTriggers.forEach(trigger => {
                trigger.addEventListener('click', () => {
                    const targetTabId = trigger.getAttribute('data-tab-trigger');

                    // Update button classes
                    tabTriggers.forEach(btn => {
                        const isTarget = btn.getAttribute('data-tab-trigger') === targetTabId;

                        // Toggle classes for "Abas em Caixa" style (boxed tabs)
                        btn.classList.toggle('bg-white', isTarget);
                        btn.classList.toggle('border-2', isTarget);
                        btn.classList.toggle('border-black', isTarget);
                        btn.classList.toggle('neo-shadow-sm', isTarget);
                        
                        btn.classList.toggle('hover:bg-white/50', !isTarget);
                    });

                    // Show/hide content panels
                    tabContents.forEach(content => {
                        const contentId = content.getAttribute('data-tab-content');
                        content.classList.toggle('hidden', contentId !== targetTabId);
                    });
                });
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new SidebarManager();
    new DropdownManager();
    new TabsManager();
});
