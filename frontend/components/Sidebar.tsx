"use client"; 
// This marks the component as a Client Component (required because we use state + event handlers)

import Image from "next/image";
// Import Next.js optimized Image component

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
    <aside className="flex h-screen w-64 flex-col justify-between border-r border-gray-200 bg-[#EEE3D2] px-4 py-6">
      <div>
      {/* LOGO + WEBSITE NAME SECTION */}
      <div className="mb-8 flex items-center gap-3 px-2">
        <Image
          src="/elements/logo_remeals.png" // Path to logo
          alt="ReMeals logo"               // Alt text for accessibility
          width={48}                       // Logo width in pixels
          height={48}                      // Logo height in pixels
          priority                         // Load this image immediately
        />

        {/* Website Name */}
        <span className="text-xl font-extrabold text-gray-900">
          ReMeals
        </span>
      </div>

      {/* NAVIGATION BUTTONS */}
      <nav className="flex flex-col gap-2">
        {tabs.map((t) => {
          // Check whether this button is the currently selected one
          const isActive = activeTab === t;

          return (
            <button
              key={t}                   // Unique key for each button
              onClick={() => onTabChange(t)} // Clicking button switches the main content
              className={[
                // Basic button styling
                "rounded-xl px-4 py-3 text-left text-base font-semibold transition",

                // If active → white background with shadow
                isActive
                  ? "bg-white text-gray-900 shadow-sm"

                  // If inactive → gray text, but turns white on hover
                  : "text-gray-700 hover:bg-white/70 hover:text-gray-900",
              ].join(" ")}
            >
              Part {t}  {/* Button label (Part 1, Part 2, … Part 7) */}
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