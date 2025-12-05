"use client"; 
// This marks the component as a Client Component (required because we use state + event handlers)

// Props definition: Sidebar receives the active tab number and a function to change tabs
type SidebarProps = {
  activeTab: number;                  // Which tab is currently selected
  onTabChange: (tab: number) => void; // Function to update the selected tab
  onAuthClick: () => void;            // callback for auth button
};

export default function Sidebar({
  activeTab,
  onTabChange,
  onAuthClick,
}: SidebarProps) {
  // Create an array [1, 2, 3, 4, 5, 6, 7] for the nav buttons
  const tabs = Array.from({ length: 7 }, (_, i) => i + 1);

  return (
    // Sidebar container: flex-col + justify-between lets us push the auth button to the bottom
    <aside
        className="
            sticky top-4            /* lock sidebar position */
            z-10                    
            m-4                     
            flex h-[calc(100vh-2rem)] w-64 flex-col justify-between
            rounded-3xl             
            bg-white/75             
            px-4 py-6
            shadow-2xl shadow-black/15 
            border border-black/5    
            "
    >
      <div>
      {/* LOGO + WEBSITE NAME SECTION */}
      
      <div className="mb-5 flex items-center pt-3 px-4">
        <span className="text-2xl font-semibold text-[#111828]">
          Re-Meals
        </span>
      </div>


      {/* NAVIGATION BUTTONS */}
      <nav className="flex flex-col gap-1 mt-2">
  {tabs.map((t) => {
    const isActive = activeTab === t;

    return (
      <button
        key={t}
        onClick={() => onTabChange(t)}
        className={[
          "flex items-center rounded-lg px-4 py-3 text-left text-base font-medium transition-colors",

          // ACTIVE → yellow background + dark text
          isActive
            ? "bg-[#F9DE84] text-gray-900"
            // HOVER (inactive) → light yellow background + dark text
            : "text-gray-700 hover:bg-[#F9DE84]/50 hover:text-gray-900",
        ].join(" ")}
      >
        Part {t}
      </button>
    );
  })}
</nav>
      </div>

      {/* Bottom section: Sign up / Login button */}
      <div className="mt-6 border-t border-gray-300 pt-4">
        <button
            onClick={onAuthClick}
            className="w-full rounded-xl bg-gray-900 px-4 py-3 text-center text-sm font-semibold text-white transition hover:bg-gray-800"
        >
            Sign up / Login
        </button>

      </div>

    </aside>
  );
}
