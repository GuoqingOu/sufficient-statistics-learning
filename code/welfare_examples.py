"""Teaching calculations only. Python 3, standard library, no empirical data."""

from math import isfinite


def positive(value, name):
    if not isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")


def top_tax_rate(a, e, welfare_weight):
    """No income effects; other simplifying assumptions are in note 02."""
    positive(a, "a")
    positive(e, "e")
    if not 0 <= welfare_weight < 1:
        raise ValueError("This teaching example requires 0 <= weight < 1")
    return (1 - welfare_weight) / (1 - welfare_weight + a * e)


def acr_ratio(domestic_before, domestic_after, theta):
    """W_after / W_before, conditional on ACR assumptions and given shares."""
    positive(theta, "theta")
    for share in (domestic_before, domestic_after):
        if not 0 < share <= 1:
            raise ValueError("Domestic shares must lie in (0, 1]")
    return (domestic_after / domestic_before) ** (-1 / theta)


def main():
    print("TEACHING INPUTS; these are not estimated policy effects.\n")
    print("Unit tax: q(t) = 100 - 2*t")
    for tax in (0, 10, 11):
        quantity = 100 - 2 * tax
        print(f"t={tax:2d}: q={quantity:3d}, revenue={tax*quantity:3d}, DWL={tax**2:3d}")
    print(f"W(11)-W(10)={-(11**2 - 10**2)}, local approximation={-2*10}")

    a, e, weight = 1.5, 0.3, 0.2
    rate = top_tax_rate(a, e, weight)
    derivative = -a * (1 - weight) / (1 - weight + a * e) ** 2
    se = abs(derivative) * 0.05
    print(f"\nTop tax rate={rate:.4f}; if e=0.5: {top_tax_rate(a, 0.5, weight):.4f}")
    print(f"Only e uncertain: SE={se:.4f}; 95% delta interval=({rate-1.96*se:.4f}, {rate+1.96*se:.4f})")
    print(f"Semi-elasticity conversion: e={-(-0.5)*(1-0.4):.4f}")

    marginal_utility_gap = (100 / 80) ** 2 - 1
    print(f"\nCRRA marginal utility gap={marginal_utility_gap:.4f}; approximation={2*(100-80)/100:.4f}")
    wtp, gross_cost, fiscal_return = 150, 100, 40
    net_cost = gross_cost - fiscal_return
    if net_cost <= 0:
        raise ValueError("Do not interpret a nonpositive-cost policy with an ordinary MVPF ratio")
    print(f"MVPF={wtp / net_cost:.4f}; net fiscal cost={net_cost}")

    print("\nACR, theta=4:")
    print(f"0.8 -> 0.7 domestic share: welfare change={100*(acr_ratio(0.8, 0.7, 4)-1):.4f}%")
    print(f"Autarky loss relative to open: {100*(1-acr_ratio(0.8, 1, 4)):.4f}%")
    print(f"Open gain relative to autarky: {100*(acr_ratio(1, 0.8, 4)-1):.4f}%")


if __name__ == "__main__":
    main()
