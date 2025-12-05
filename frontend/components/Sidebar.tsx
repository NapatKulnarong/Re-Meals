"use client";

import { FaceSmileIcon } from "@heroicons/react/24/outline";

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
  const primaryTabs = [
    {
      id: 1,
      label: "Donate",
      icon: (
        <svg
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.6"
          className="h-5 w-5"
        >
          <path
            d="M12 21s-6.5-3.5-8.5-7.5C1.8 9.5 3.9 6 7 6c2 0 3 .8 4 2 1-1.2 2-2 4-2 3.1 0 5.2 3.5 3.5 7.5C18.5 17.5 12 21 12 21Z"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      ),
    },
    {
      id: 2,
      label: "Request food",
      icon: (
        <FaceSmileIcon className="h-6 w-6" />
      ),
    },
  ];
  const secondaryTabs = tabs.filter((t) => t > 2);

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
      <nav className="flex flex-col gap-4 mt-2">
        <div className="grid grid-cols-2 gap-3">
          {primaryTabs.map((tab) => {
            const isActive = activeTab === tab.id;
            const palette =
              tab.id === 1
                ? {
                    activeBg: "bg-[#E9F7EF]",
                    activeBorder: "border-[#A7D6B6]",
                    activeText: "text-[#1F4D36]",
                    inactiveBorder: "border-[#DCE9E1]",
                    inactiveText: "text-[#2F4F3A]",
                    iconActive: "bg-white text-[#1F4D36]",
                    iconInactive: "bg-[#F0F7F2] text-[#3C6E52]",
                    hoverBorder: "hover:border-[#A7D6B6]",
                  }
                : {
                    activeBg: "bg-[#FFF3E6]",
                    activeBorder: "border-[#F3C7A0]",
                    activeText: "text-[#8B4C1F]",
                    inactiveBorder: "border-[#F2E3D6]",
                    inactiveText: "text-[#6B4A2A]",
                    iconActive: "bg-white text-[#C4641A]",
                    iconInactive: "bg-[#FFF5EC] text-[#C4641A]",
                    hoverBorder: "hover:border-[#F3C7A0]",
                  };
            return (
              <button
                key={tab.id}
                onClick={() => onTabChange(tab.id)}
                className={[
                  "aspect-square w-full rounded-2xl border text-sm font-semibold shadow-sm transition duration-200",
                  isActive
                    ? `${palette.activeBorder} ${palette.activeBg} ${palette.activeText} shadow-md`
                    : `${palette.inactiveBorder} bg-white ${palette.inactiveText} ${palette.hoverBorder} hover:shadow`,
                ].join(" ")}
              >
                <div className="flex h-full flex-col items-center justify-center gap-2">
                  <span
                    className={[
                      "flex h-10 w-10 items-center justify-center rounded-full text-lg transition",
                      isActive ? palette.iconActive : palette.iconInactive,
                    ].join(" ")}
                  >
                    {tab.icon}
                  </span>
                  <span>{tab.label}</span>
                </div>
              </button>
            );
          })}
        </div>

        <div className="flex flex-col gap-1">
          {secondaryTabs.map((t) => {
            const isActive = activeTab === t;

            return (
              <button
                key={t}
                onClick={() => onTabChange(t)}
                className={[
                  "flex items-center rounded-lg px-4 py-3 text-left text-base font-medium transition-colors",
                  isActive
                    ? "bg-[#F9DE84] text-gray-900"
                    : "text-gray-700 hover:bg-[#F9DE84]/50 hover:text-gray-900",
                ].join(" ")}
              >
                Part {t}
              </button>
            );
          })}
        </div>
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
