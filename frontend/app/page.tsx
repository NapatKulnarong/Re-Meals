"use client";

import Image from 'next/image'

export default function Home() {
  return (
    <main className="min-h-screen items-center justify-center bg-[#EEE3D2]">
      <header className='flex items-center gap-3 p-6'>
        <Image
          src="/elements/logo_remeals.png"
          alt="ReMeals logo"
          width={65}
          height={65}
          priority
        />
      </header>
      <section className="rounded-xl bg-white p-10 shadow-lg text-center">
        <h1 className="text-4xl font-bold text-gray-900">ReMeals</h1>
        <p className="mt-4 text-gray-600">
          Welcome to your new Next.js app. Customize this section to introduce the product, add CTA buttons, etc.
        </p>
      </section>
      
    </main>
  )
}