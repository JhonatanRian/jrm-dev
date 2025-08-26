const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');
const sidebarToggle = document.getElementById('sidebar-toggle');
const toggleIconOpen = document.getElementById('toggle-icon-open');
const toggleIconClose = document.getElementById('toggle-icon-close');

const COLLAPSED_WIDTH_CLASS = 'w-20';
const EXPANDED_WIDTH_CLASS = 'w-72';
const COLLAPSED_MARGIN = '80px';
const EXPANDED_MARGIN = '288px';
const COLLAPSED_BUTTON_LEFT = '60px';
const EXPANDED_BUTTON_LEFT = '268px';

function setSidebarState(isCollapsed) {
    sidebar.classList.toggle('sidebar-collapsed', isCollapsed);

    sidebar.classList.toggle(EXPANDED_WIDTH_CLASS, !isCollapsed);
    sidebar.classList.toggle(COLLAPSED_WIDTH_CLASS, isCollapsed);

    mainContent.style.marginLeft = isCollapsed ? COLLAPSED_MARGIN : EXPANDED_MARGIN;
    sidebarToggle.style.left = isCollapsed ? COLLAPSED_BUTTON_LEFT : EXPANDED_BUTTON_LEFT;

    toggleIconOpen.classList.toggle('hidden', !isCollapsed);
    toggleIconClose.classList.toggle('hidden', isCollapsed);

    // Fecha todos os submenus quando o sidebar é recolhido
    if (isCollapsed) {
        document.querySelectorAll('[data-submenu-list]').forEach(submenu => {
            submenu.classList.add('hidden');
            const icon = submenu.previousElementSibling.querySelector('[data-submenu-icon]');
            if (icon) icon.classList.remove('rotate-180');
        });
    }
}

sidebarToggle.addEventListener('click', () => {
    setSidebarState(sidebar.classList.contains(EXPANDED_WIDTH_CLASS));
});

// Lógica do Submenu
document.querySelectorAll('[data-submenu-trigger]').forEach(trigger => {
    trigger.addEventListener('click', () => {
        // Não expandir submenu se o sidebar estiver recolhido
        if (sidebar.classList.contains('sidebar-collapsed')) {
            setSidebarState(false); // Expande o sidebar
        }

        const submenuList = trigger.nextElementSibling;
        const submenuIcon = trigger.querySelector('[data-submenu-icon]');

        submenuList.classList.toggle('hidden');
        submenuIcon.classList.toggle('rotate-180');
    });
});

// Estado inicial (Expandido por padrão)
setSidebarState(false);
