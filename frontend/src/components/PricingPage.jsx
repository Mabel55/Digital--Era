import React, { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import PublicNavbar from './PublicNavbar';
import { 
  GraduationCap, Check, Zap, Crown, Rocket, Star, 
  BookOpen, Bot, Award, Terminal, ArrowRight, Sparkles,
  Shield, Clock, Users
} from 'lucide-react';

const PricingPage = () => {
  const navigate = useNavigate();
  const { token, user } = useAuth();
  const [searchParams] = useSearchParams();
  const [billingCycle, setBillingCycle] = useState('monthly');
  const [loading, setLoading] = useState(null);
  const [subscription, setSubscription] = useState(null);

  const paymentStatus = searchParams.get('payment');

  useEffect(() => {
    if (token) {
      fetchSubscription();
    }
  }, [token]);

  const fetchSubscription = async () => {
    try {
      const res = await fetch('/payments/subscription', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setSubscription(data);
      }
    } catch (e) {
      console.error('Failed to fetch subscription:', e);
    }
  };

  const handleUpgrade = async (plan) => {
    if (!token) {
      navigate('/onboarding');
      return;
    }

    setLoading(plan);
    try {
      const res = await fetch(`/payments/create-checkout?plan=${plan}`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      
      if (res.ok) {
        const data = await res.json();
        window.location.href = data.checkout_url;
      } else {
        const err = await res.json();
        alert(err.detail || 'Something went wrong. Please try again.');
      }
    } catch (e) {
      alert('Connection error. Please try again.');
    } finally {
      setLoading(null);
    }
  };

  const handleManageSubscription = async () => {
    alert('To manage or cancel your Paystack subscription, please click the "Manage Subscription" link in the receipt email sent to you by Paystack.');
  };

  const plans = [
    {
      id: 'free',
      name: 'Free',
      price: 0,
      description: 'Perfect for getting started',
      icon: <BookOpen size={28} strokeWidth={1.5} />,
      color: 'var(--text2)',
      features: [
        { text: '3 beginner courses', included: true },
        { text: '3 AI tutor messages/day', included: true },
        { text: 'Community forum', included: true },
        { text: 'Basic code editor', included: true },
        { text: 'All courses & tracks', included: false },
        { text: 'Downloadable certificates', included: false },
        { text: 'Unlimited AI tutor', included: false },
        { text: 'Guided projects', included: false },
      ]
    },
    {
      id: billingCycle === 'yearly' ? 'pro_yearly' : 'pro_monthly',
      name: 'Pro',
      price: billingCycle === 'yearly' ? 79 : 9.99,
      description: 'For serious learners ready to level up',
      icon: <Crown size={28} strokeWidth={1.5} />,
      color: 'var(--accent)',
      popular: true,
      features: [
        { text: 'All courses & learning paths', included: true },
        { text: 'Unlimited AI tutor', included: true },
        { text: 'Downloadable certificates', included: true },
        { text: 'Guided projects', included: true },
        { text: 'Skill assessments & badges', included: true },
        { text: 'Priority support', included: true },
        { text: 'LinkedIn certifications', included: true },
        { text: billingCycle === 'yearly' ? 'Save 34% vs monthly' : 'Cancel anytime', included: true },
      ]
    }
  ];

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '60px 24px', maxWidth: '1100px', margin: '0 auto', width: '100%' }}>
        
        {/* Success / Cancel banners */}
        {paymentStatus === 'success' && (
          <div style={{
            background: 'rgba(0, 229, 160, 0.1)', border: '1px solid var(--accent)',
            borderRadius: '12px', padding: '16px 24px', marginBottom: '32px',
            display: 'flex', alignItems: 'center', gap: '12px', color: 'var(--accent)'
          }}>
            <Sparkles size={20} /> <strong>Welcome to Pro!</strong> Your subscription is now active. Enjoy unlimited access!
          </div>
        )}
        {paymentStatus === 'canceled' && (
          <div style={{
            background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239,68,68,0.3)',
            borderRadius: '12px', padding: '16px 24px', marginBottom: '32px',
            color: 'var(--danger)'
          }}>
            Payment was canceled. You can try again anytime.
          </div>
        )}

        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '48px', position: 'relative' }}>
          {/* Decorative glow */}
          <div style={{
            position: 'absolute', top: '-100px', left: '50%', transform: 'translateX(-50%)',
            width: '600px', height: '600px',
            background: 'radial-gradient(circle, rgba(0, 229, 160, 0.08) 0%, transparent 70%)',
            borderRadius: '50%', pointerEvents: 'none', zIndex: 0
          }}></div>
          
          <div style={{ position: 'relative', zIndex: 1 }}>
            <div style={{
              display: 'inline-flex', alignItems: 'center', gap: '8px',
              padding: '6px 16px', background: 'var(--surface)', border: '1px solid var(--border)',
              borderRadius: '100px', marginBottom: '24px',
              boxShadow: '0 4px 20px rgba(0,0,0,0.2)'
            }}>
              <Zap size={14} color="var(--accent)" />
              <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text2)' }}>Simple, transparent pricing</span>
            </div>

            <h1 style={{ 
              fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 52px)', 
              fontWeight: 800, marginBottom: '16px', lineHeight: 1.1 
            }}>
              Invest in Your <span style={{ color: 'var(--accent)', textShadow: '0 0 30px var(--accent-glow)' }}>Future</span>
            </h1>
            <p style={{ color: 'var(--text2)', fontSize: '17px', maxWidth: '550px', margin: '0 auto', lineHeight: 1.6 }}>
              Start free, upgrade when you're ready. No hidden fees, cancel anytime.
            </p>
          </div>
        </div>



        {/* Plans Grid */}
        <div style={{ 
          display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', 
          gap: '24px', maxWidth: '800px', margin: '0 auto 64px' 
        }}>
          {plans.map((plan) => {
            const isCurrentPlan = subscription?.plan === plan.id || 
              (plan.id === 'free' && (!subscription || subscription.plan === 'free'));
            const isPro = subscription?.is_pro;

            return (
              <div
                key={plan.id}
                style={{
                  background: 'var(--surface)',
                  border: plan.popular ? '2px solid var(--accent)' : '1px solid var(--border)',
                  borderRadius: '20px',
                  padding: '32px',
                  position: 'relative',
                  transition: 'transform 0.2s, box-shadow 0.2s',
                  boxShadow: plan.popular ? '0 8px 40px rgba(0, 229, 160, 0.12)' : 'none'
                }}
                onMouseEnter={(e) => { e.currentTarget.style.transform = 'translateY(-4px)'; }}
                onMouseLeave={(e) => { e.currentTarget.style.transform = 'translateY(0)'; }}
              >
                {/* Popular badge */}
                {plan.popular && (
                  <div style={{
                    position: 'absolute', top: '-14px', left: '50%', transform: 'translateX(-50%)',
                    background: 'linear-gradient(135deg, var(--accent), #3b82f6)',
                    color: '#fff', fontWeight: 700, fontSize: '12px',
                    padding: '5px 20px', borderRadius: '100px',
                    boxShadow: '0 4px 15px rgba(0,229,160,0.3)',
                    display: 'flex', alignItems: 'center', gap: '6px'
                  }}>
                    <Star size={12} fill="white" /> MOST POPULAR
                  </div>
                )}

                {/* Plan header */}
                <div style={{ marginBottom: '24px' }}>
                  <div style={{ 
                    width: '48px', height: '48px', borderRadius: '12px',
                    background: plan.popular ? 'rgba(0,229,160,0.1)' : 'var(--surface2)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: plan.color, marginBottom: '16px'
                  }}>
                    {plan.icon}
                  </div>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '24px', fontWeight: 700, marginBottom: '6px' }}>
                    {plan.name}
                  </h3>
                  <p style={{ color: 'var(--text2)', fontSize: '14px' }}>{plan.description}</p>
                </div>

                {/* Price */}
                <div style={{ marginBottom: '28px' }}>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: '4px' }}>
                    <span style={{ fontSize: '48px', fontWeight: 800, fontFamily: 'var(--font-display)' }}>
                      ${plan.price === 0 ? '0' : plan.price}
                    </span>
                    {plan.price > 0 && (
                      <span style={{ color: 'var(--text2)', fontSize: '15px' }}>
                        /{billingCycle === 'yearly' ? 'year' : 'month'}
                      </span>
                    )}
                  </div>
                  {plan.price > 0 && billingCycle === 'yearly' && (
                    <p style={{ color: 'var(--text3)', fontSize: '13px', marginTop: '4px' }}>
                      That's just ${(79/12).toFixed(2)}/month
                    </p>
                  )}
                </div>

                {/* CTA Button */}
                {isCurrentPlan ? (
                  <button
                    style={{
                      width: '100%', padding: '14px 24px', borderRadius: '12px',
                      background: 'var(--surface2)', color: 'var(--text2)',
                      border: '1px solid var(--border)', cursor: 'default',
                      fontWeight: 600, fontSize: '15px', fontFamily: 'inherit',
                      display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px'
                    }}
                    disabled
                  >
                    <Check size={18} /> Current Plan
                  </button>
                ) : isPro && plan.id === 'free' ? (
                  <button
                    onClick={handleManageSubscription}
                    style={{
                      width: '100%', padding: '14px 24px', borderRadius: '12px',
                      background: 'transparent', color: 'var(--text2)',
                      border: '1px solid var(--border)', cursor: 'pointer',
                      fontWeight: 600, fontSize: '15px', fontFamily: 'inherit'
                    }}
                  >
                    Manage Subscription
                  </button>
                ) : (
                  <button
                    onClick={() => plan.price === 0 ? navigate('/onboarding') : handleUpgrade(plan.id)}
                    disabled={loading === plan.id}
                    style={{
                      width: '100%', padding: '14px 24px', borderRadius: '12px',
                      background: plan.popular ? 'var(--accent)' : 'var(--surface2)',
                      color: plan.popular ? '#0d0f14' : 'var(--text)',
                      border: plan.popular ? 'none' : '1px solid var(--border)',
                      cursor: 'pointer', fontWeight: 700, fontSize: '15px', fontFamily: 'inherit',
                      display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                      transition: 'opacity 0.2s',
                      opacity: loading === plan.id ? 0.6 : 1
                    }}
                  >
                    {loading === plan.id ? 'Redirecting to checkout...' : (
                      plan.price === 0 ? (
                        <><Rocket size={18} /> Get Started Free</>
                      ) : (
                        <><ArrowRight size={18} /> Upgrade to Pro</>
                      )
                    )}
                  </button>
                )}

                {/* Features */}
                <div style={{ marginTop: '28px', borderTop: '1px solid var(--border)', paddingTop: '24px' }}>
                  <p style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text2)', marginBottom: '16px', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    {plan.price === 0 ? "What's included" : "Everything in Free, plus"}
                  </p>
                  <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {plan.features.map((feature, idx) => (
                      <li key={idx} style={{ 
                        display: 'flex', alignItems: 'center', gap: '10px', 
                        fontSize: '14px',
                        color: feature.included ? 'var(--text)' : 'var(--text3)',
                        textDecoration: feature.included ? 'none' : 'line-through'
                      }}>
                        {feature.included ? (
                          <div style={{
                            width: '20px', height: '20px', borderRadius: '50%',
                            background: plan.popular ? 'rgba(0,229,160,0.15)' : 'var(--surface2)',
                            display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0
                          }}>
                            <Check size={12} color={plan.popular ? 'var(--accent)' : 'var(--text2)'} />
                          </div>
                        ) : (
                          <div style={{
                            width: '20px', height: '20px', borderRadius: '50%',
                            background: 'var(--surface2)',
                            display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0
                          }}>
                            <span style={{ fontSize: '12px', color: 'var(--text3)' }}>–</span>
                          </div>
                        )}
                        {feature.text}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            );
          })}
        </div>

        {/* Trust Badges */}
        <div style={{ 
          display: 'flex', justifyContent: 'center', gap: '40px', flexWrap: 'wrap',
          marginBottom: '64px', padding: '32px', borderRadius: '16px',
          background: 'var(--surface)', border: '1px solid var(--border)'
        }}>
          {[
            { icon: <Shield size={20} />, text: 'Secure payments via Paystack' },
            { icon: <Clock size={20} />, text: 'Cancel anytime, no lock-in' },
            { icon: <Users size={20} />, text: 'Trusted by learners worldwide' },
          ].map((badge, idx) => (
            <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--text2)', fontSize: '14px' }}>
              <div style={{ color: 'var(--accent)' }}>{badge.icon}</div>
              {badge.text}
            </div>
          ))}
        </div>

        {/* FAQ Section */}
        <div style={{ maxWidth: '700px', margin: '0 auto 60px' }}>
          <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '32px', fontWeight: 800, textAlign: 'center', marginBottom: '36px' }}>
            Frequently Asked <span style={{ color: 'var(--accent)' }}>Questions</span>
          </h2>

          {[
            {
              q: 'Can I try Pro features before paying?',
              a: 'Absolutely! Start with our Free plan and explore 3 beginner courses. When you\'re ready for more, upgrade to Pro for full access to everything.'
            },
            {
              q: 'What payment methods do you accept?',
              a: 'We accept all major credit and debit cards (Visa, Mastercard, American Express) through Paystack\'s secure payment platform.'
            },
            {
              q: 'Can I cancel my subscription?',
              a: 'Yes, you can cancel anytime from your dashboard. You\'ll keep Pro access until the end of your billing period.'
            },
            {
              q: 'Do I get a certificate for every course?',
              a: 'Pro subscribers receive a downloadable, verifiable certificate upon completing each course. Free users can complete courses but certificates require Pro.'
            },
            {
              q: 'Is there a student discount?',
              a: 'Our yearly plan already saves you 34%. For bulk school/university pricing, contact us at support@digital-era.live.'
            }
          ].map((faq, idx) => (
            <div key={idx} style={{
              padding: '24px', marginBottom: '12px',
              background: 'var(--surface)', border: '1px solid var(--border)',
              borderRadius: '12px'
            }}>
              <h3 style={{ fontSize: '16px', fontWeight: 600, marginBottom: '8px', color: 'var(--text)' }}>{faq.q}</h3>
              <p style={{ color: 'var(--text2)', fontSize: '14px', lineHeight: 1.6 }}>{faq.a}</p>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer style={{
        padding: '32px', borderTop: '1px solid var(--border)',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: 'var(--surface)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><GraduationCap size={18} /> Digital Era</span>
        </div>
        <p style={{ color: 'var(--text2)', fontSize: '13px' }}>© 2026 Digital Era. Founded by Arua Mabel Chinasa.</p>
      </footer>
    </div>
  );
};

export default PricingPage;
