"use client"; 

import Image from 'next/image'
import {useState} from "react"; // React hook for tracking active tab

import Sidebar from '@/components/Sidebar';

// Component to display the content of the active tab
function TabContent({ tab }: {tab: number}) {
  return (
    // Simple card-style content area
    <div className="rounded-xl bg-white p-10 shadow text-center">
      <h1 className="text-3xl font-bold text-gray-900">
        Part {tab}   {/* Display which part is active */}
      </h1>

      <p className="mt-3 text-gray-600">
        This is a blank page for Part {tab}. You’ll add real content later.
      </p>
    </div>
  );
}


export default function Home() {
  // React state: keeps track of which tab is selected
  // Default = Part 1
  const [activeTab, setActiveTab] = useState(1);

  return (

    <main className="min-h-screen items-center justify-center bg-white">

      {/* --- SIDEBAR SECTION --- */}
      {/* Pass activeTab + function to update it */}
      <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />

      {/* --- MAIN CONTENT AREA --- */}
      <section className="flex-1 p-8">
         {/* Dynamically shows content of current tab */}
         <TabContent tab={activeTab} />
       </section> 
    </main>
  )
}