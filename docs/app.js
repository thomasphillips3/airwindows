/**
 * Airwindows Documentation Web Application
 * Interactive plugin browser and documentation viewer
 */

// State management
const state = {
    plugins: [],
    categories: [],
    currentView: 'home',
    currentPlugin: null,
    currentCategory: null,
    searchTerm: '',
    currentFilter: 'all'
};

// Initialize application
document.addEventListener('DOMContentLoaded', async () => {
    console.log('Initializing Airwindows Documentation...');
    
    try {
        await loadData();
        initializeEventListeners();
        initializeTheme();
        initializeBackToTop();
        renderView('home');
        
        console.log(`Loaded ${state.plugins.length} plugins and ${state.categories.length} categories`);
    } catch (error) {
        console.error('Failed to initialize application:', error);
        showError('Failed to load plugin data. Please refresh the page.');
    }
});

// Load plugin and category data
async function loadData() {
    const [pluginsResponse, categoriesResponse] = await Promise.all([
        fetch('data/plugins.json'),
        fetch('data/categories.json')
    ]);
    
    state.plugins = await pluginsResponse.json();
    state.categories = await categoriesResponse.json();
    
    // Update stats
    document.getElementById('totalPlugins').textContent = state.plugins.length;
    document.getElementById('categoryCount').textContent = state.categories.length;
}

// Initialize event listeners
function initializeEventListeners() {
    // Navigation buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const view = e.target.dataset.view;
            renderView(view);
        });
    });
    
    // Search input
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', debounce((e) => {
        state.searchTerm = e.target.value.toLowerCase();
        if (state.currentView === 'plugins' || state.currentView === 'home') {
            renderPluginsList();
        }
    }, 300));
    
    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            state.currentFilter = e.target.dataset.filter;
            renderPluginsList();
        });
    });
    
    // Back buttons
    document.getElementById('backBtn').addEventListener('click', () => {
        renderView('plugins');
    });
    
    document.getElementById('categoryBackBtn').addEventListener('click', () => {
        renderView('categories');
    });
    
    // Theme toggle
    document.getElementById('themeToggle').addEventListener('click', toggleTheme);
}

// Theme management
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const icon = document.querySelector('.theme-icon');
    icon.textContent = theme === 'dark' ? '🌙' : '☀️';
}

// Back to top button
function initializeBackToTop() {
    const backToTop = document.getElementById('backToTop');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// View rendering
function renderView(viewName) {
    // Update state
    state.currentView = viewName;
    
    // Update navigation
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.view === viewName);
    });
    
    // Hide all views
    document.querySelectorAll('.view').forEach(view => {
        view.classList.remove('active');
    });
    
    // Show requested view
    const viewMap = {
        'home': 'homeView',
        'categories': 'categoriesView',
        'plugins': 'pluginsView',
        'plugin-detail': 'pluginDetailView',
        'category-detail': 'categoryDetailView'
    };
    
    const viewId = viewMap[viewName];
    if (viewId) {
        document.getElementById(viewId).classList.add('active');
    }
    
    // Render content based on view
    switch (viewName) {
        case 'home':
            renderHome();
            break;
        case 'categories':
            renderCategories();
            break;
        case 'plugins':
            renderPluginsList();
            break;
    }
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Home view
function renderHome() {
    renderFeaturedPlugins();
    renderCategoriesPreview();
}

function renderFeaturedPlugins() {
    const container = document.getElementById('featuredPlugins');
    const featured = state.plugins
        .filter(p => p.is_recommended)
        .slice(0, 6);
    
    container.innerHTML = featured.map(plugin => createPluginCard(plugin)).join('');
    
    // Add click listeners
    container.querySelectorAll('.plugin-card').forEach((card, index) => {
        card.addEventListener('click', () => showPluginDetail(featured[index]));
    });
}

function renderCategoriesPreview() {
    const container = document.getElementById('categoriesPreview');
    const categories = state.categories.slice(0, 6);
    
    container.innerHTML = categories.map(cat => createCategoryCard(cat)).join('');
    
    // Add click listeners
    container.querySelectorAll('.category-card').forEach((card, index) => {
        card.addEventListener('click', () => showCategoryDetail(categories[index]));
    });
}

// Categories view
function renderCategories() {
    const container = document.getElementById('categoriesList');
    container.innerHTML = state.categories.map(cat => createCategoryCard(cat)).join('');
    
    // Add click listeners
    container.querySelectorAll('.category-card').forEach((card, index) => {
        card.addEventListener('click', () => showCategoryDetail(state.categories[index]));
    });
}

// Plugins list view
function renderPluginsList() {
    const container = document.getElementById('pluginsList');
    const countEl = document.getElementById('pluginCount');
    
    // Filter plugins
    let filtered = state.plugins;
    
    // Apply filter
    if (state.currentFilter !== 'all') {
        filtered = filtered.filter(p => {
            switch (state.currentFilter) {
                case 'latest': return p.is_latest;
                case 'recommended': return p.is_recommended;
                case 'basic': return p.is_basic;
                default: return true;
            }
        });
    }
    
    // Apply search
    if (state.searchTerm) {
        filtered = filtered.filter(p => 
            p.name.toLowerCase().includes(state.searchTerm) ||
            p.description.toLowerCase().includes(state.searchTerm) ||
            p.categories.some(c => c.toLowerCase().includes(state.searchTerm))
        );
    }
    
    // Update count
    countEl.textContent = `Showing ${filtered.length} of ${state.plugins.length} plugins`;
    
    // Render
    if (filtered.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🔍</div>
                <p>No plugins found matching your criteria</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = filtered.map(plugin => createPluginListItem(plugin)).join('');
    
    // Add click listeners
    container.querySelectorAll('.plugin-list-item').forEach((item, index) => {
        item.addEventListener('click', () => showPluginDetail(filtered[index]));
    });
}

// Plugin detail view
function showPluginDetail(plugin) {
    state.currentPlugin = plugin;
    
    const container = document.getElementById('pluginDetail');
    container.innerHTML = createPluginDetail(plugin);
    
    // Initialize Mermaid diagrams
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({ startOnLoad: true, theme: 'dark' });
        mermaid.contentLoaded();
    }
    
    renderView('plugin-detail');
}

// Category detail view
function showCategoryDetail(category) {
    state.currentCategory = category;
    
    const container = document.getElementById('categoryDetail');
    const categoryPlugins = state.plugins.filter(p => 
        p.categories.includes(category.name)
    );
    
    container.innerHTML = `
        <div class="plugin-detail-header">
            <h2 class="plugin-detail-title">${category.name}</h2>
            <p class="hero-description">${category.description}</p>
        </div>
        
        <div class="detail-meta">
            <div class="meta-item">
                <span class="meta-label">Total Plugins</span>
                <span class="meta-value">${category.plugin_count}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Latest</span>
                <span class="meta-value">${categoryPlugins.filter(p => p.is_latest).length}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Recommended</span>
                <span class="meta-value">${categoryPlugins.filter(p => p.is_recommended).length}</span>
            </div>
        </div>
        
        <div class="plugin-grid">
            ${categoryPlugins.map(p => createPluginCard(p)).join('')}
        </div>
    `;
    
    // Add click listeners
    container.querySelectorAll('.plugin-card').forEach((card, index) => {
        card.addEventListener('click', () => showPluginDetail(categoryPlugins[index]));
    });
    
    renderView('category-detail');
}

// Component creators
function createCategoryCard(category) {
    return `
        <div class="category-card">
            <div class="category-card-header">
                <h3 class="category-name">${category.name}</h3>
                <span class="category-count">${category.plugin_count}</span>
            </div>
            <p class="category-description">${category.description}</p>
        </div>
    `;
}

function createPluginCard(plugin) {
    const tags = [];
    if (plugin.is_latest) tags.push('<span class="tag latest">Latest</span>');
    if (plugin.is_recommended) tags.push('<span class="tag recommended">Recommended</span>');
    if (plugin.is_basic) tags.push('<span class="tag basic">Basic</span>');
    
    return `
        <div class="plugin-card">
            <div class="plugin-card-header">
                <h3 class="plugin-name">${plugin.name}</h3>
            </div>
            ${tags.length > 0 ? `<div class="plugin-tags">${tags.join('')}</div>` : ''}
            <p class="plugin-description">${plugin.description}</p>
            <div class="plugin-categories">
                ${plugin.categories.map(cat => `<span class="category-badge">${cat}</span>`).join('')}
            </div>
        </div>
    `;
}

function createPluginListItem(plugin) {
    const tags = [];
    if (plugin.is_latest) tags.push('<span class="tag latest">Latest</span>');
    if (plugin.is_recommended) tags.push('<span class="tag recommended">Recommended</span>');
    if (plugin.is_basic) tags.push('<span class="tag basic">Basic</span>');
    
    return `
        <div class="plugin-list-item">
            <div class="plugin-list-info">
                <h3 class="plugin-list-name">${plugin.name}</h3>
                <p class="plugin-list-desc">${plugin.description}</p>
            </div>
            <div class="plugin-tags">
                ${tags.join('')}
            </div>
        </div>
    `;
}

function createPluginDetail(plugin) {
    const tags = [];
    if (plugin.is_latest) tags.push('<span class="tag latest">Latest</span>');
    if (plugin.is_recommended) tags.push('<span class="tag recommended">Recommended</span>');
    if (plugin.is_basic) tags.push('<span class="tag basic">Basic</span>');
    
    return `
        <div class="plugin-detail-header">
            <h2 class="plugin-detail-title">${plugin.name}</h2>
            ${tags.length > 0 ? `<div class="plugin-tags">${tags.join('')}</div>` : ''}
        </div>
        
        <div class="detail-meta">
            <div class="meta-item">
                <span class="meta-label">Categories</span>
                <span class="meta-value">${plugin.categories.join(', ')}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Source Code</span>
                <span class="meta-value">
                    <a href="https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/${plugin.name}" 
                       target="_blank" style="color: var(--primary-color)">View on GitHub</a>
                </span>
            </div>
        </div>
        
        <div class="plugin-detail-content">
            <div class="detail-section">
                <h3>Description</h3>
                <p>${plugin.description}</p>
            </div>
            
            ${plugin.full_description ? `
                <div class="detail-section">
                    <h3>Detailed Information</h3>
                    <p>${plugin.full_description}</p>
                </div>
            ` : ''}
            
            ${createSignalFlowDiagram(plugin)}
            
            <div class="detail-section">
                <h3>Related Plugins</h3>
                <div class="plugin-categories">
                    ${getRelatedPlugins(plugin).map(p => 
                        `<span class="category-badge" style="cursor: pointer" onclick="window.showPluginByName('${p.name}')">${p.name}</span>`
                    ).join('')}
                </div>
            </div>
        </div>
    `;
}

function createSignalFlowDiagram(plugin) {
    // Determine plugin type and create appropriate diagram
    const category = plugin.categories[0];
    let diagram = '';
    
    if (category === 'Consoles') {
        diagram = `
            graph LR
                A[Input] --> B[Gain Staging]
                B --> C[Saturation]
                C --> D[Summing]
                D --> E[Output]
                style A fill:#6366f1
                style E fill:#6366f1
        `;
    } else if (category === 'Dynamics') {
        diagram = `
            graph LR
                A[Input] --> B[Detector]
                B --> C[Gain Computer]
                C --> D[Gain Reduction]
                A --> D
                D --> E[Output]
                style A fill:#6366f1
                style E fill:#6366f1
        `;
    } else if (category === 'Reverb') {
        diagram = `
            graph LR
                A[Input] --> B[Early Reflections]
                A --> C[Diffusion Network]
                C --> D[Feedback Loop]
                D --> C
                B --> E[Mix]
                D --> E
                A --> E
                E --> F[Output]
                style A fill:#6366f1
                style F fill:#6366f1
        `;
    } else if (category === 'Filter') {
        diagram = `
            graph LR
                A[Input] --> B[Filter Stage]
                B --> C[Resonance]
                C --> D[Output Stage]
                D --> E[Output]
                style A fill:#6366f1
                style E fill:#6366f1
        `;
    } else {
        diagram = `
            graph LR
                A[Input] --> B[Processing]
                B --> C[Output]
                style A fill:#6366f1
                style C fill:#6366f1
        `;
    }
    
    return `
        <div class="detail-section">
            <h3>Signal Flow</h3>
            <div class="mermaid">
                ${diagram}
            </div>
        </div>
    `;
}

function getRelatedPlugins(plugin) {
    // Find plugins in same categories
    const related = state.plugins.filter(p => 
        p.name !== plugin.name && 
        p.categories.some(cat => plugin.categories.includes(cat))
    );
    
    // Return up to 8 related plugins
    return related.slice(0, 8);
}

// Global function to show plugin by name (for related plugins)
window.showPluginByName = function(name) {
    const plugin = state.plugins.find(p => p.name === name);
    if (plugin) {
        showPluginDetail(plugin);
    }
};

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function showError(message) {
    console.error(message);
    alert(message); // Simple error handling for now
}

